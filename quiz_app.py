import json

# Load questions from JSON file
with open("questions.json", "r") as file:
    questions = json.load(file)

score = 0

# Loop through each question
for index, q in enumerate(questions, 1):
    print(f"\nQuestion {index}: {q['question']}")
    for i, option in enumerate(q['options'], 1):
        print(f"{i}. {option}")
    
    # Get user answer
    try:
        answer = int(input("Your answer (1-4): "))
        if q['options'][answer - 1].strip().lower() == q['answer'].strip().lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}")
    except:
        print("❌ Invalid input. Skipped.")

# Final feedback
print("\n🎉 Quiz Completed!")
print(f"Your final score: {score} out of {len(questions)}")

if score == 10:
    print("🏆 Perfect Score!")
elif score >= 7:
    print("👏 Good job!")
else:
    print("📘 Keep practicing!")
