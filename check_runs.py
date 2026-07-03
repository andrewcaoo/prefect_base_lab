import asyncio
from prefect.client import get_client

async def main():
    async with get_client() as client:
        runs = await client.read_flow_runs(limit=10)
        for r in runs:
            if r.state_name == "Scheduled":
                print(f"Run {r.name}: state={r.state_name}, expected={r.expected_start_time}, deployment={r.deployment_id}")

asyncio.run(main())
