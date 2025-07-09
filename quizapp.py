
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },
    {
        "question": "Who is the father of Computer Science?",
        "options": ["A. Bill Gates", "B. Charles Babbage", "C. Alan Turing", "D. Steve Jobs"],
        "answer": "B"
    }
]

score = 0

# Quiz Logic
for i, q in enumerate(quiz):
    print(f"\nQ{i+1}: {q['question']}")
    for opt in q["options"]:
        print(opt)
    user_ans = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    if user_ans == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer: {q['answer']}")

# Final Result
print(f"\n🎉 Quiz Completed! Your Score: {score}/{len(quiz)}")
