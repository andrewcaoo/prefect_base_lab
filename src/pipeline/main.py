from prefect import flow, serve

@flow(name="Hello_World_Pipeline", log_prints=True)
def hello_flow():
    print("hello world")

def main():
    # to_deployment() does NOT block — it just creates the deployment object
    dep1 = hello_flow.to_deployment(name="prefect-docker-guide-1", cron="0 1 * * *", tags=["abc"])
    dep2 = hello_flow.to_deployment(name="prefect-docker-guide-2", cron="0 2 * * *", tags=["abc"])
    dep3 = hello_flow.to_deployment(name="prefect-docker-guide-3", cron="0 3 * * *", tags=["abc"])
    dep4 = hello_flow.to_deployment(name="prefect-docker-guide-4", cron="0 4 * * *", tags=["abc"])
    dep5 = hello_flow.to_deployment(name="prefect-docker-guide-5", cron="0 5 * * *", tags=["abc"])

    # serve() listens for ALL deployments at once (this is the only blocking call)
    serve(dep1, dep2, dep3, dep4, dep5)


if __name__ == "__main__":
    main()
