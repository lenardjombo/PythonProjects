# quiz_game.py

# Function to ask a question, display options, and check if the answer is correct
def ask_question(question, options, correct_answer):
    print('''A quiz game developed by jombo
    The basic quiz game has 6 questions to be answered alongside 6 answers
    Enjoy!'''
    print("\n" + question)
    for i, option in enumerate(options):
        print(f"{chr(65 + i)}. {option}")  # Display options as A, B, C, D
    answer = input("Your answer (A/B/C/D): ").upper()
    
    # Ensure the answer is one of the valid options
    while answer not in ["A", "B", "C", "D"]:
        answer = input("Invalid input. Please enter A, B, C, or D: ").upper()

    return answer == correct_answer

# Main function to run the quiz game
def main():
    # List of questions, each with options and the correct answer
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "London", "Paris", "Rome"],
            "correct_answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "B"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "Jane Austen"],
            "correct_answer": "A"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct_answer": "D"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["Oxygen", "Gold", "Silver", "Iron"],
            "correct_answer": "A"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
            "correct_answer": "B"
        }
    ]

    score = 0  # Initialize score

    # Iterate through each question
    for i in questions:
        # Ask the question and check the answer
        if ask_question(i["question"], i["options"], i["correct_answer"]):
            print("Correct!")
            score += 1  # Increment score for correct answer
        else:
            print("Incorrect.")

    # Display final score
    print(f"\nYour final score is: {score}/{len(questions)}")

# Check if the script is run directly
if __name__ == "__main__":
    main()
