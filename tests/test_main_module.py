# tests/test_main_module.py
import os
import csv
import unittest
from src.extractor import main_module
from src.extractor.logger import log

"""
Main test driver to test output of currently selected model_name for given set
of input text for all the attributes. Adapt the input texts (or read from 
json/csv file if needed), attributes and expected results
"""
model_name = "dummy"

class TestMainModule(unittest.TestCase):
    def test_all_inputs(self):
        log.info(f"Enter test_all_inputs: model_name={model_name}")
        self.test_count = 0
        self.fail_count = 0
        self.attribute_fail_counts = {}
        test_data_list = self._init_from_csv()
        attributes = self._get_attributes(test_data_list)
        log.info(f"Testing {len(test_data_list)} input_text for {len(attributes)} attributes")
        for test_data in test_data_list:
            self._test_one_input(test_data)
        
        self._print_stats(test_data_list)
        self._save_csv(test_data_list, attributes)
        self.assertEqual(self.fail_count, 0, f"{self.fail_count} of {self.test_count} tests failed")

    def _init_from_csv(self):
        test_data_file = "tests/test_data.csv"
        if not os.path.exists(test_data_file):
            raise ValueError(f"'{test_data_file}' not found.")
        
        test_data_list = []
        with open(test_data_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                test_data = {"input_text": "", "attributes": {}}
                test_data_list.append(test_data)
                for key in row:
                    if key == "input_text":
                        test_data[key] = row[key]
                    else:
                        test_data["attributes"][key] = {"expected": row[key]}
        return test_data_list
        
    def _test_one_input(self, test_data):
        for attribute in test_data["attributes"]:
            attribute_info = test_data["attributes"][attribute]
            attribute_info["actual_output"] = main_module.main(
                test_data["input_text"], attribute, model_name)
            self.test_count += 1
            if attribute_info["actual_output"] != attribute_info["expected"]:
                self.fail_count += 1
                if attribute not in self.attribute_fail_counts:
                    self.attribute_fail_counts[attribute] = 0
                self.attribute_fail_counts[attribute] += 1

    def _print_stats(self, test_data_list):
        total_count = len(test_data_list)
        overall_pass_count = 0
        overall_total_count = 0
        for attribute in self.attribute_fail_counts:
            pass_count =  total_count - self.attribute_fail_counts[attribute]
            pass_perc = 0 if total_count == 0 else 100.0 * (pass_count / total_count)
            pass_perc = round(pass_perc, 0)
            log.info(f"Attribute {attribute} pass_perc={pass_perc}% ({pass_count} of {total_count})")
            overall_pass_count += pass_count
            overall_total_count += total_count
            
        overall_pass_perc = 0 if overall_total_count == 0 else 100.0 * (overall_pass_count / overall_total_count)
        overall_pass_perc = round(overall_pass_perc, 0)
        log.info(f"Overall pass_perc={pass_perc}% ({overall_pass_count} of {overall_total_count})")

    def _save_csv(self, test_data_list, attributes):
        with open('tests/test_results.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            header = ['input_text']
            for attribute in attributes:
                header.append(f"{attribute} expected")
                header.append(f"{attribute} actual")
                header.append(f"{attribute} status")
            writer.writerow(header)
            
            for test_data in test_data_list:
                row = []
                row.append(test_data["input_text"])
                for attribute in test_data["attributes"]:
                    attribute_info = test_data["attributes"][attribute]
                    expected = attribute_info["expected"]
                    actual = attribute_info["actual_output"]
                    status = "pass" if expected == actual else "failed"
                    row.append(expected)
                    row.append(actual)
                    row.append(status)
                writer.writerow(row)
                
    def _get_attributes(self, test_data_list):
        return dict.keys(test_data_list[0]["attributes"]) if len(test_data_list) > 0 else []
        

        
if __name__ == '__main__':
    unittest.main()