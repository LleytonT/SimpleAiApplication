import pandas as pd
import random

# Expanded subjects and sample questions/answers
subjects = {
    'Mathematics': [
        ("Differentiate f(x) = 3x^2 + 2x + 1.", "f'(x) = 6x + 2"),
        ("Evaluate the integral of 1/x dx.", "The integral of 1/x is ln|x| + C."),
        ("Solve the equation: sin(2x) = 1 for 0 ≤ x ≤ π.", "x = π/4, 3π/4"),
        ("If f(x) = x^3 - 4x, find the critical points.", "Critical points are x = 0, 2, -2."),
        ("Find the derivative of ln(x^2 + 1).", "The derivative is (2x)/(x^2 + 1).")
    ],
    'English': [
        ("What is the significance of the green light in 'The Great Gatsby'?", "The green light symbolizes Gatsby's unattainable dreams and hopes."),
        ("Discuss the theme of revenge in 'Hamlet'.", "The theme of revenge is central, as Hamlet seeks to avenge his father's death, but it leads to tragedy."),
        ("Analyze the use of symbolism in George Orwell's '1984'.", "Symbols such as Big Brother, the Party, and the paperweight represent surveillance and control."),
        ("What is the role of Ophelia in 'Hamlet'?", "Ophelia represents innocence and her madness reflects the chaos in the Danish court."),
        ("Compare and contrast the characters of Daisy Buchanan and Jordan Baker in 'The Great Gatsby'.", "Daisy is portrayed as fragile and trapped by society, while Jordan is independent and modern.")
    ],
    'Physics': [
        ("State and explain the law of conservation of momentum.", "In a closed system, the total momentum before and after a collision is conserved."),
        ("Calculate the potential energy of a 5 kg object raised to a height of 10 meters (g = 9.8 m/s^2).", "Potential energy = mgh = 5 × 9.8 × 10 = 490 J."),
        ("What is the difference between speed and velocity?", "Speed is a scalar quantity (magnitude only), while velocity is a vector (magnitude and direction)."),
        ("Explain the photoelectric effect.", "The photoelectric effect occurs when light shines on a metal surface, causing the emission of electrons."),
        ("What is the Heisenberg Uncertainty Principle?", "It states that it is impossible to simultaneously know the exact position and momentum of a particle.")
    ],
    'Chemistry': [
        ("Write the balanced equation for the combustion of methane.", "CH4 + 2O2 → CO2 + 2H2O"),
        ("Explain Le Chatelier's principle.", "Le Chatelier's principle states that if a system at equilibrium is disturbed, it will shift to counteract the disturbance."),
        ("What is the IUPAC name for CH3CH2OH?", "The IUPAC name is ethanol."),
        ("Calculate the molarity of a solution containing 5 moles of solute in 2 liters of solution.", "Molarity = 5 moles / 2 liters = 2.5 M."),
        ("What are the key differences between covalent and ionic bonds?", "Covalent bonds involve sharing electrons, while ionic bonds involve the transfer of electrons.")
    ],
    'Biology': [
        ("Describe the process of DNA replication.", "DNA replication involves the unwinding of the double helix, followed by complementary base pairing to form two identical strands."),
        ("Explain the role of enzymes in metabolism.", "Enzymes act as biological catalysts, speeding up chemical reactions without being consumed."),
        ("What is the structure and function of the cell membrane?", "The cell membrane is a phospholipid bilayer that controls the movement of substances in and out of the cell."),
        ("Define the term 'photosynthesis'.", "Photosynthesis is the process by which plants convert sunlight into chemical energy (glucose) using carbon dioxide and water."),
        ("What is the role of the lymphatic system in immunity?", "The lymphatic system helps transport immune cells and removes waste from the body's tissues.")
    ],
    'Economics': [
        ("What is price elasticity of demand and how is it calculated?", "Price elasticity of demand measures how the quantity demanded of a good responds to a change in price. It is calculated as the percentage change in quantity demanded divided by the percentage change in price."),
        ("Explain the concept of comparative advantage in international trade.", "Comparative advantage occurs when a country can produce a good at a lower opportunity cost than another country, leading to beneficial trade."),
        ("What are the causes of inflation?", "Inflation can be caused by demand-pull factors, cost-push factors, or excessive money supply."),
        ("What is the function of the Reserve Bank of Australia?", "The Reserve Bank of Australia is responsible for setting monetary policy, including controlling inflation and maintaining financial stability."),
        ("Explain the impact of government subsidies on supply and demand.", "Government subsidies reduce the cost of production, increasing supply and lowering the market price.")
    ]
}

# Generate the expanded dataset
data = []

for subject, qa_pairs in subjects.items():
    for question, answer in qa_pairs:
        data.append({'input': question, 'label': subject, 'answer': answer})

# Create a DataFrame
df = pd.DataFrame(data)

# Save the expanded dataset to a CSV file
df.to_csv('hsc_tutor_training_data.csv', index=False)

print("Expanded HSC tutor training data generated and saved to 'hsc_tutor_training_data.csv'.")
