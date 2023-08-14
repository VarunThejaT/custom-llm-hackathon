import replicate

training = replicate.trainings.create(
  version="a16z-infra/llama-2-7b-chat:7b0bfc9aff140d5b75bacbed23e91fd3c34b01a1e958d32132de6e0a19796e2c",
  input={
    "train_data": "https://raw.githubusercontent.com/VarunThejaT/custom-llm-hackathon/master/replicate_sample.jsonl",
  },
  destination="varunthejat/npctest"
)

print(training)