print("hyyy,walcome to our calculator")

num1= float(input("enter the first number: "))
num2=float(input("enter the second number: "))
print("enter 1 for adition \n enter 2 for mainus \n enter 3 division \n enter 4 for square first_num^second_num\n enter 5 for multiplication ")
entered_number = input("enter any number you want : ")

if entered_number == '1' : 
 print( num1 + num2)

if entered_number == '2' :
 print(num1 - num2)

if entered_number == '3':
    if num1>num2 :
          print("your ans is:", num1 / num2)
    if num2>num1 :
        print("your ans is : ", num2 / num1 )

if entered_number == '4':
 print("your ans is:", num1 ** num2)

if entered_number == '5' :
 print("your ans is:", num1 * num2)

# import pandas as pd # type: ignore
# from sklearn.model_selection import train_test_split # type: ignore
# from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
# from sklearn.linear_model import PassiveAggressiveClassifier # type: ignore
# from sklearn.metrics import accuracy_score # type: ignore
# import joblib # type: ignore

# # Load dataset
# data_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/fake_or_real_news.csv"
# df = pd.read_csv(data_url)

# # Prepare data
# X = df['text']
# y = df['label']

# # Convert labels to binary
# y = y.map({'FAKE': 0, 'REAL': 1})

# # Split the dataset
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# # Vectorize text data
# vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
# X_train_vec = vectorizer.fit_transform(X_train)
# X_test_vec = vectorizer.transform(X_test)

# # Train model
# model = PassiveAggressiveClassifier(max_iter=50)
# model.fit(X_train_vec, y_train)

# # Evaluate
# score = accuracy_score(y_test, model.predict(X_test_vec))
# print("Model Accuracy: {:.2f}%".format(score * 100))

# # Save model and vectorizer
# joblib.dump(model, "fake_news_model.pkl")
# joblib.dump(vectorizer, "vectorizer.pkl")

# # Simple CLI interface
# def classify_news(text):
#     model = joblib.load("fake_news_model.pkl")
#     vectorizer = joblib.load("vectorizer.pkl")
#     input_vec = vectorizer.transform([text])
#     prediction = model.predict(input_vec)[0]
#     return "REAL" if prediction == 1 else "FAKE"

# # Test the classifier
# if __name__ == "__main__":
#     print("\n--- Fake News Detector ---")
#     news_text = input("Enter news text to classify: ")
#     if news_text.strip():
#         result = classify_news(news_text)
#         print(f"\nThe news is: {result}")
#     else:
#         print("\nNo text entered.")


