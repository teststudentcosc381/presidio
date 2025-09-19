from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

# Initialize the engine:
engine = AnonymizerEngine()

# Invoke the anonymize function with the text, 
# analyzer results (potentially coming from presidio-analyzer) and
# Operators to get the anonymization output:
result = engine.anonymize(
    text="My name is Siyuan, Siyuan Jiang",
    analyzer_results=[
        RecognizerResult(entity_type="PERSON", start=11, end=17, score=0.8),
        RecognizerResult(entity_type="PERSON", start=19, end=31, score=0.8),
    ],
    operators={"PERSON": OperatorConfig("replace", {"new_value": "sjiang1"})},
)

print(result)