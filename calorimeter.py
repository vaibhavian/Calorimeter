options = ["Bomb Calorimeter", "Boys Calorimeter"]  # List of options

# Displaying the options
print("Select an option:")
for i, option in enumerate(options):
  print(f"{i + 1}. {option}")

# Asking the user for input
choice = int(input("Enter your choice (1-2): "))
  
# Validating the input
if choice < 1 or choice > len(options):
  print("Invalid choice!")
else:
  selected_option = options[choice - 1]
  print(f"You selected: {selected_option}")

# Proceed with the selected option
if selected_option == "Bomb Calorimeter":
  # Code for Bomb Calorimeter
  print("Determine GCV for Solid or non-volatile liquid fuel...")

  def gcv(W, w, T2, T1, x):
    gcv = (W + w) * (T2 -
                     T1) / x  # Calculate the gross calorific value in cal/gm
    return gcv

# Example usage

  W = int(input("Enter the weight of water (gm): "))
  w = int(input("Enter the water equivalent (gm): "))
  T2 = float(input("Enter the final temperature of water (degree celcius): "))
  T1 = float(
    input("Enter the initial temperature of water (degree celcius): "))
  x = float(
    input("Enter the weight of fuel taken in stainless steel crucible (gm): "))

  result = round(gcv(W, w, T2, T1, x), 2)
  if (T2 - T1) > 0:
    print(f"The gross calorific value of the fuel is  is {result} cal/gm.")
  else:
    print('Initial Temperature is greater than final temperature.')

elif selected_option == "Boys Calorimeter":
  # Code for Boys Calorimeter
  print("Determine GCV for Volatile liquid or Gaseous fuel...")

  def gcv(W, T2, T1, V):
    gcv = W * (T2 - T1) / V  # Calculate the gross calorific value in Kcal/m³
    return gcv

# Example usage

  W = int(input("Enter the weight of water (Kg): "))
  T2 = float(input("Enter the final temperature of water (degree celcius): "))
  T1 = float(
    input("Enter the initial temperature of water (degree celcius): "))
  V = float(
    input("Enter the volume of fuel taken in stainless steel crucible (m³): "))

  result = round(gcv(W, T2, T1, V), 2)
  if (T2 - T1) > 0:
    print(f"The gross calorific value of the fuel is  is {result} Kcal/m³.")
  else:
    print('Initial Temperature is greater than final temperature.')
