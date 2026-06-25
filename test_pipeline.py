from core.pipeline import ScanPipeline


pipeline = ScanPipeline()

context = pipeline.run(
    "amazon.com"
)

print()

print("Collector Results")

print()

for name, result in context.collector_results.items():

    print(name)

    print(result)

    print()