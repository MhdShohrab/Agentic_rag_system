from agent.agent_pipeline import agent_pipeline


def run_tests():

    #Same user → memory works
    user_id = "user_1"

    queries = [

        # MEMORY TEST (conversation)
        # ...............................
        "What is AI?",
        "Explain it in simple terms",
        "Give an example",

        #  MULTI-STEP TEST
        # ................................
        "Compare it with latest AI trends",
        "Find total cost from document",
        "Convert 100 USD to INR",
        "Analyze the document",

        # EDGE CASE
        # ..............................
        "who is md shohrab"
    ]

    for q in queries:
        result = agent_pipeline(q, user_id=user_id)

        print("\n.....................................")
        print(f"Query       : {result['query']}")
        print(f"Type        : {result['type']}")
        print(f"Tool Used   : {result['tool_used']}")
        print(f"Answer      : {result['answer']}")


if __name__ == "__main__":
    run_tests()