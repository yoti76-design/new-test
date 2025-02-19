from pymongo import MongoClient

# Replace the following with your MongoDB connection details
mongo_uri = "mongodb://your_username:your_password@your_host:your_port/your_database"
client = MongoClient(mongo_uri)

# Access the database
db = client['your_database']

# Access a specific collection
collection = db['your_collection']

# Example operation: Fetch all documents from the collection
documents = collection.find()

# Print the documents
for document in documents:
    print(document)

# Close the connection when done
client.close()