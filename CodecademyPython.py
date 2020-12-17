# Python 3 Codecademy Labs
# Functions
def repeat_stuff(stuff, num_repeats=10):
    return stuff*num_repeats

lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)

print(song)

def sing_song():
  print("You may say I'm a dreamer")
  print("But I'm not the only one")
  print("I hope some day you'll join us")
  print("And the world will be as one")
  
# call sing_song() below:
sing_song()
sing_song()

def loading_screen():
  print("This page is loading...")

loading_screen()

def about_this_computer():	
    print("This computer is running on Whackintosh version Everest Puma")
print("This is your desktop")

about_this_computer()

def mult_two_add_three(number):

    print(number*2 + 3)

# Call mult_two_add_three() here:
mult_two_add_three(1)
mult_two_add_three(5)
mult_two_add_three(-1)
mult_two_add_three(0)

def mult_x_add_y(number, x, y):
    print(number*x + y)
mult_x_add_y(5,2,3)
mult_x_add_y(1,3,1)

# Define create_spreadsheet():
def create_spreadsheet(title, row_count=10 ):
  print("Creating a spreadsheet called "+title+ " with " +str(row_count)+ " rows")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")
create_spreadsheet("Applications")

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
calculate_age(2049, 1993)
my_age = calculate_age(2049, 1993)
calculate_age(2049, 1953)
dads_age = calculate_age(2049, 1953)
print(f"I am {my_age } years old and my dad is {dads_age } years  old")

def get_boundaries(target,margin):
    low_limit= target-margin
    high_limit= margin+target
    return low_limit,high_limit
get_boundaries(100,20)
low, high = get_boundaries(100,20)

current_year = 2048
def calculate_age(birth_year):
    age = current_year - birth_year
    return age
print(calculate_age(1970))

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  return(f_temp-32) * 5/9 
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
  return(c_temp* 9/5) + 32
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

def get_energy(mass, c=3*10**8):
  return mass * c ** 2
bomb_energy = get_energy(bomb_mass)
  
print(f"A 1kg bomb supplies {bomb_energy} Joules")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
    return force *distance
train_work = get_work(train_mass,train_acceleration,train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")