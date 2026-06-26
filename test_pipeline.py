from core.pipeline import ScanPipeline

pipeline = ScanPipeline()

context = pipeline.run("amazon.com")

print("\nEvidence Package\n")

print("=" * 60)

from pprint import pprint

pprint(
    context.evidence_package
)