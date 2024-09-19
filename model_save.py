import pickle

# Save model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
