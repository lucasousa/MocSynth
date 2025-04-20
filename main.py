from src.simulator import generate_synthetic_data
from src.utils import save_to_json

if __name__ == "__main__":
    providers_config = [
        {"name": "AWS", "services": ["EC2", "S3", "Lambda"]},
        {"name": "Azure", "services": ["VM", "BlobStorage", "Functions"]},
        {
            "name": "GCP",
            "services": ["ComputeEngine", "CloudStorage", "CloudFunctions"],
        },
    ]

    dataset = generate_synthetic_data(
        days=2,
        interval_minutes=60,
        proportions=[60, 30, 10],
        providers=providers_config,
    )
    print(f"Generated {len(dataset)} data points.")
    save_to_json(dataset, filename="synthetic_data.json")
