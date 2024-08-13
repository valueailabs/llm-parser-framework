# llm-parser-framework

This is a non-working sample project to explain the structure of a framework that can be created to solve the below described problem.

## Problem
Extract different attributes from an input text. The input text does not follow any strict template. This is typically human-written and could have many attributes missing or written in very different ways.

## Requirements
- *Multiple LLMs*: The parsing of text and extracting the required attributes is done using LLMs. A lot of experimentation may be required to select an LLM. The framework must support easy swapping of the LLM.
- *Attribute specific prompts*: The LLM is given a prompt that contains instructions on how to extract a given attribute. The prompt sent for each attribute will be different. 
- *Automated testing*: Prompts will have to be fine-tuned. Different LLMs have to be tried. The LLM may have to be changed over a period of time. As multiple rounds of experimentation will be required with different LLMs and prompts, extensive test automation will be required.

## Design
1. Support for multiple LLMs using factory pattern: see `llms/llm_base.py` that implements common interface for all LLMs. Individual LLM classes (`llms/*model.py`) initialize the specific LLM. `llm/llm_factory.py` implements the factory method to get the LLM based on the model_name. Please delete unnecessary model classes and add the needed ones. Adapt the llm_factory accordingly.
2. Prompts are defined per attribute. Adapt the `prompts/*.txt` accordingly. Delete the dummy files provided here and create new ones with the name of the attribute you would like to extract from the input text.
3. Code flow starts from `extractor/main_module.py`. The `main()` method in this file extracts one attribute from the input test using the given model.
4. `tests/test_main_module.py` is the main test driver. This takes `test_data.csv` as input. Each row in the input csv file contains test input and expected output for each attribute. The test driver calls the extractor for each input text and attribute combination - if there are 100 rows in the CSV file and 5 columns (input text + 4 attributes), the extractor is called 100*4 times. Test passes only if all the actual outputs match their respective expected values. The actual outputs received are recorded in `test_results.csv` file.

## Folder Structure

```
llm_parser_framework/
│
├── src/
│   ├── extractor/
│   │   ├── __init__.py
│   │   ├── main_module.py   /* Code flow starts here */
│   │   └── logger.py
│   │
│   ├── llms/
│   │   ├── __init__.py
│   │   ├── llm_interface.py  /* All LLMs implement this interface */
│   │   ├── llm_factory.py    /* Factory is used from main_module to get the llm */
│   │   └── dummyemodel.py    /* LLM specific implementation 0 for testing */
│   │   ├── gptmodel.py       /* LLM specific implementation 1 */
│   │   ├── llama2model.py    /* LLM specific implementation 2 */
│   │   └── coheremodel.py    /* LLM specific implementation 3 */
│   │
│   ├── prompts/              /* One file per attribute */
│   │   ├── attribute1.txt
│   │   ├── attribute2.txt
│   │   └── ...
│   │
├── tests/
│   ├── test_main_module.py   /* Main test driver */
│   ├── test_data.csv         /* Data for the test driver test driver */
│   └── ...
│
├── requirements.txt
├── README.md
```

## First time setup
1. Go to your repo base folder: `cd path/to/repo/parent/folder`
2. Clone this repo: `git clone https://github.com/valueailabs/llm-parser-framework.git`
3. `cd llm-parser-framework`
4. Check if Python is installed by executing `python3 --version`. If not installed, install from https://www.python.org/downloads/
5. Create Python virtual environment in this folder: `python3 -m venv venv`
6. Source the virtual environment: `source venv/bin/activate`
7. Update pip in venv: `pip install --upgrade pip`
8. Install all the needed Python libraries in venv: `pip install -r requirements.txt`

## Testing the dummy framework

You can test the framework with dummy inputs and a dummy LLM by executing the following command:
`python -m unittest discover -s tests`
This will execute the `TestMainModule.test_all_inputs` method. 6 of 9 tests are expected to fail with the dummy configuration.
