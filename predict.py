import replicate
output = replicate.run(
    "varunthejat/npctest:0c563b3679f89c667063e868b78eb117da554c078c2599cd11cb35799ded7aa7",
    input={"prompt": "azure nexus"}
)
# The varunthejat/npctest model can stream output as it's running.
# The predict method returns an iterator, and you can iterate over that output.
for item in output:
    # https://replicate.com/varunthejat/npctest/versions/0c563b3679f89c667063e868b78eb117da554c078c2599cd11cb35799ded7aa7/api#output-schema
    print(item)