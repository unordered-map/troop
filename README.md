# troop - a LLM management library

## Folder Structure

```
troop/
├── models/                  # Model-related logic (loading, inference)
│   ├── __init__.py         # Makes "models" a package
│   ├── base.py             # Abstract base class for models
│   ├── openai_model.py     # OpenAI API model integration
│   └── hf_model.py         # Hugging Face local model integration
│
├── core/                   # Core functionalities
│   ├── __init__.py        # Makes "core" a package
│   └── manager.py         # Main LLMManager class (switches between providers)
│
├── config.py              # Configuration settings
├── __init__.py           # Makes "troop" a package
├── examples/             # Example scripts to test
└── tests/                # Unit tests
```

## Usage

Run the module:
```bash
python -m troop
```