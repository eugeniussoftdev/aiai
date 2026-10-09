def call_agent(system: str, brief: str, tools: list) -> str:
    response_message = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system=system,
        messages=[{"role": "user", "content": brief}],
    )

    # return 


def orchestrate(user_message: str) -> str:
    plan = ["auth", "payments"]

    results = {}

    if "auth" in plan:
        results["auth"] = call_agent(
            system="",
            brief="",
            toolts=[]
        )
    
    if "payments" in plan:
        results["payments"] = call_agent(
            system="",
            brief="",
            toolts=[]
        )
