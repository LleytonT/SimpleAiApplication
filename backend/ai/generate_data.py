import pandas as pd

# Define the existing data (or load it if you have it)
data = {
    'Mathematics': [
        ("What is the quadratic formula?", "The quadratic formula is x = (-b ± √(b²-4ac)) / 2a."),
        ("Factor the polynomial x² - 5x + 6.", "(x - 2)(x - 3)"),
        ("What is the area of a circle with a radius of 3?", "The area is π * r² = 28.27."),
        ("Find the derivative of f(x) = x³ - 2x² + x - 5.", "f'(x) = 3x² - 4x + 1"),
        ("Evaluate the integral ∫ (2x + 3) dx.", "The integral is x² + 3x + C."),
        ("How do you calculate the standard deviation?", "Standard deviation is calculated as the square root of the variance."),
        ("What is the volume of a sphere with a radius of 4?", "Volume = (4/3)πr³ = 268.08."),
        ("What is the formula for the area of a triangle?", "Area = 1/2 * base * height."),
        ("Solve the equation: 3x + 5 = 20.", "x = 5."),
        ("If f(x) = x² + 2x, find f(3).", "f(3) = 15."),
    ],
    'English': [
        ("What is the structure of a persuasive essay?", "Introduction, Body Paragraphs, Conclusion."),
        ("Analyze the use of foreshadowing in 'Of Mice and Men'.", "Foreshadowing is shown through various hints throughout the novel."),
        ("Discuss the main themes of 'Pride and Prejudice'.", "Themes include social class, love, and reputation."),
        ("What are the key features of a Shakespearean sonnet?", "14 lines, iambic pentameter, and a specific rhyme scheme."),
        ("How do you develop a thesis statement?", "A thesis statement should state your position and the main points of your argument."),
        ("What are the main ideas in 'The Road Not Taken'?", "The poem discusses choices and their impact on life."),
        ("Compare the protagonists in '1984' and 'Brave New World'.", "Both deal with control and freedom but in different societal structures."),
        ("What is the significance of the setting in 'The Great Gatsby'?", "The setting reflects the themes of wealth and moral decay."),
        ("What is the purpose of literary devices?", "Literary devices enhance meaning and add depth to the text."),
        ("Explain the theme of isolation in 'Frankenstein'.", "Isolation affects both Victor and the creature, leading to tragedy."),
    ],
    'Physics': [
        ("What is Newton's first law of motion?", "An object at rest stays at rest, and an object in motion stays in motion unless acted upon by a net force."),
        ("Explain the concept of friction and its types.", "Friction is a force resisting motion; types include static, kinetic, and rolling."),
        ("What is the first law of thermodynamics?", "Energy cannot be created or destroyed, only transformed."),
        ("Describe how lenses work.", "Lenses bend light rays to converge or diverge them, forming images."),
        ("What is Ohm's Law?", "V = IR, where V is voltage, I is current, and R is resistance."),
        ("What are the properties of sound waves?", "Sound waves are longitudinal, can travel through solids, liquids, and gases, and have frequency and amplitude."),
        ("What is the difference between scalar and vector quantities?", "Scalars have magnitude only, while vectors have both magnitude and direction."),
        ("What is the relationship between frequency and wavelength?", "Frequency and wavelength are inversely proportional in wave motion."),
        ("Explain the photoelectric effect.", "The photoelectric effect occurs when light causes the emission of electrons from a material."),
        ("Define kinetic energy and its formula.", "Kinetic energy is the energy of motion, KE = 1/2 mv²."),
    ]
}

# Create a DataFrame and save it
expanded_data = []

for subject, qa_pairs in data.items():
    for question, answer in qa_pairs:
        expanded_data.append({'input': question, 'label': subject, 'answer': answer})

# Create a DataFrame
df_expanded = pd.DataFrame(expanded_data)

# Save the expanded dataset to a CSV file
df_expanded.to_csv('hsc_tutor_training_data_v2.csv', index=False)

print("Expanded HSC tutor training data generated and saved to 'expanded_hsc_tutor_training_data_v2.csv'.")
