import json

class SymbolicPromptValidator:
    """
    A utility to validate prompts against a 5-part framework.

    The 5-part framework consists of:
    1. Intent: The core objective of the prompt.
    2. Context: Background information or data.
    3. Persona: The desired persona for the AI's response.
    4. Format: The required output format (e.g., JSON, XML, text).
    5. Constraints: Any limitations or rules to follow.
    """

    FRAMEWORK_KEYS = ["intent", "context", "persona", "format", "constraints"]

    def __init__(self, prompt):
        """
        Initializes the validator with a prompt.

        Args:
            prompt (str or dict): The prompt to validate. If a string,
                                  it should be a JSON string.
        """
        if isinstance(prompt, str):
            try:
                self.prompt_data = json.loads(prompt)
            except json.JSONDecodeError:
                raise ValueError("Prompt string must be a valid JSON.")
        elif isinstance(prompt, dict):
            self.prompt_data = prompt
        else:
            raise TypeError("Prompt must be a JSON string or a dictionary.")

    def validate(self):
        """
        Validates the prompt against the 5-part framework.

        Returns:
            tuple: A tuple containing a boolean indicating success and a list
                   of validation messages.
        """
        missing_keys = [key for key in self.FRAMEWORK_KEYS if key not in self.prompt_data]
        if missing_keys:
            return False, [f"Missing framework key: {key}" for key in missing_keys]

        empty_keys = [key for key, value in self.prompt_data.items() if key in self.FRAMEWORK_KEYS and not value]
        if empty_keys:
            return False, [f"Framework key is empty: {key}" for key in empty_keys]

        return True, ["Prompt is valid."]

def main():
    """
    Demonstrates the SymbolicPromptValidator.
    """
    print("Symbolic Prompt Parser Utility")
    print("Demonstrates 5-part framework validation without proprietary binding algorithms.")
    print("-" * 20)

    # Example of a valid prompt
    valid_prompt = {
        "intent": "Generate a summary of the provided text.",
        "context": "The text is a news article about AI.",
        "persona": "An expert AI researcher.",
        "format": "A three-paragraph summary.",
        "constraints": "Avoid technical jargon."
    }

    print("Testing a valid prompt:")
    validator = SymbolicPromptValidator(valid_prompt)
    is_valid, messages = validator.validate()
    print(f"Validation result: {'Success' if is_valid else 'Failure'}")
    for msg in messages:
        print(f"- {msg}")
    print("-" * 20)


    # Example of an invalid prompt (missing 'persona')
    invalid_prompt_missing_key = {
        "intent": "Generate a summary of the provided text.",
        "context": "The text is a news article about AI.",
        "format": "A three-paragraph summary.",
        "constraints": "Avoid technical jargon."
    }

    print("Testing an invalid prompt (missing 'persona'):")
    validator = SymbolicPromptValidator(invalid_prompt_missing_key)
    is_valid, messages = validator.validate()
    print(f"Validation result: {'Success' if is_valid else 'Failure'}")
    for msg in messages:
        print(f"- {msg}")
    print("-" * 20)


    # Example of an invalid prompt (empty 'context')
    invalid_prompt_empty_key = {
        "intent": "Generate a summary of the provided text.",
        "context": "",
        "persona": "An expert AI researcher.",
        "format": "A three-paragraph summary.",
        "constraints": "Avoid technical jargon."
    }

    print("Testing an invalid prompt (empty 'context'):")
    validator = SymbolicPromptValidator(invalid_prompt_empty_key)
    is_valid, messages = validator.validate()
    print(f"Validation result: {'Success' if is_valid else 'Failure'}")
    for msg in messages:
        print(f"- {msg}")

if __name__ == "__main__":
    main()
