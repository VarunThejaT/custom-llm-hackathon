import replicate

training = replicate.trainings.create(
  version="a16z-infra/llama-2-7b-chat:058333670f2a6e88cf1b29b8183405b17bb997767282f790b82137df8c090c1f",
  input={
    "train_data": "https://storage.googleapis.com/dan-scratch-public/fine-tuning/70k_samples.jsonl",
  },
  destination="varuntheja/npctest"
)

print(training)