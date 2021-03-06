#This code assumes the user wants to design a short concrete reinforced.
#These columns DO NOT fail due to buckling.
#This program can produce SQUARE columns with reinforcing on all FOUR sides of the column.
#This program can also produce CIRCULAR columns.
#All columns are reinforced with steel bars.
#This program assumes that the compressive strength of concrete is 4 ksi
#This program assumes that the yielding strength of the rebars is 60 ksi
#The tables and figures only work for 4 ksi concrete and steel with a yielding strength of 60 ksi
#The ratio of steel reinforcement can only be between 0.01 and 0.08, inclusive.
#This program assumes a cover of 3 inches to comply with ACI code
#This program also assumes compression controlled columns are being produced

#CIRCULAR COLUMN EXAMPLE
#Initial axial load is 890 kips
#Initial moment load is 390 kip-feet
#Using spiral reinforcing

#This is the assumption made for concrete and steel
#Concrete has a compressive strength of 4 ksi
#Steel yields at 60 ksi
f_conc = 4
f_yield = 60


#This is to determine the shape of the column that will be designed
col_type = str(input("Type 'square' or 'circular' to determine the shape of the column design: "))

while col_type != 'square' and col_type != 'circular':
    col_type = str(input('Retype square or circular to determine the shape of the column design: '))


#This is to determine the forces and moments that will act on the column
p_fact = float(input('Input factored axial load in Kips: '))
m_fact = float(input('Input factored moment load in Kip-ft: '))

#This is to determine the if the ratio of steel reinforcement is known.
#This value is required to determine the gross area of the column
display("Type 'yes' or 'no'")
ratio_g = input('Is the ratio of steel reinforcement to cross sectional area known? :')

#If the ratio is not known, it is assumed to be 0.01
while ratio_g != 'yes' and ratio_g != 'no':
  display("'Type 'yes' or 'no'")
  ratio_g = input('Is the ratio of steel reinforcement to cross sectional area known? :')

if ratio_g == 'yes':
  rho_g = float(input('Input ratio of reinforcement area to cross-sectional area of column: '))
elif ratio_g == 'no':
  rho_g = 0.01

#This is to determine the spiral type that will be used for the column.
#Square columns usually have ties to prevent the reinforcing from coming out of the column.
#Circular columns usually have spirals to prevent the reinforcing from coming out of the column.
spiral_type = input("Type 'tied' or 'spiral' for type of tie reinforcing: '")

while spiral_type != 'tied' and spiral_type != 'spiral':
  spiral_type = input("'Retype 'tied' or 'spiral' for type of tie reinforcing: '")

#The phi values for either case are due to the assumption that the columns are compression controlled
#The phi values are used to determine the gross area of the column
if spiral_type == 'tied':

    phi = 0.65

    gross_area = p_fact / (0.8 * phi * (0.85 * f_conc * (1 - rho_g) + (f_yield * rho_g)))

elif spiral_type == 'spiral':

    phi = 0.75

    gross_area = p_fact / (0.85 * phi * (0.85 * f_conc * (1 - rho_g) + (f_yield * rho_g)))

#The code displays the calculated gross area of the column and the calculated core size
gross_area = round(gross_area, 0)
display('The gross area of the core is: {} square inches'.format(gross_area))

core_size = (gross_area)**0.5
core_size = round(core_size, 1)
display('The size of the column is {} inches'.format(core_size))

#The next two inputs are supposed to be larger than the calculated gross area and core size
selected_column_size = int(input('Input core size from Table A-14: '))

selected_column_area = float(input('Input area size from Table A-14: '))

#This calculation assumes a 3 inch covering around the steel bars. This is to comply with ACI code.
#This also assumes #3 bars for the tie reinforcement
#This also assumes #8 bars for the column reinforcement
inner_core = selected_column_size - 2 * 1.5 - 2 * (3/8) - (8/8)

#This is to obtain a value that will help determine which design figure to use.
gamma = round(inner_core / selected_column_size , 1)

req_k = round(p_fact / (phi * f_conc * selected_column_area) , 2)

req_r = round(m_fact * 12 / (phi * f_conc * selected_column_area * selected_column_size) , 2)

#Displays the Y and X-axis values to use for the design figure.
display('Enter table with K value: ', req_k)
display('Enter table with R value: ', req_r)

#These next conditional statements determine which figure will be used with the calculated K and R values
if gamma == 0.7:

  if col_type == 'square':
    display('Use Figure A-17')

  elif col_type == 'circular':
    display('Use Figure A-20')

elif gamma == 0.8:

  if col_type == 'square':
    display('Use Figure A-18')

  elif col_type == 'circular':
    display('Use Figure A-21')

elif gamma == 0.9:

  if col_type == 'square':
    display('Use Figure A-19')

  elif col_type == 'circular':
    display('Use Figure A-22')

#The Y-axis is the req_k value. The interval for the Y-axis is 0.04.
#The X-axis is the req_r value. The interval for the X-axis is 0.01.
rho = float(input('Input rho value from the figure given above: '))

#Determines the required area for the steel reinforcement
area_steel = rho * selected_column_area

display(round(area_steel,2))

#Required to determine if the bars fit in the column.
#This determines the size number of the bar.
#Size of bars that are used in Table A-14 are between 2 and 11.
bar_size = int(input('Type bar number from Table A-2: '))

#Required to determine if the bars fit in the column.
#This determines the amount of bars in the column.
if col_type == 'square':
  display('Number of bars has to be a multiple of 4 for even distribution of force in column.')
  number_of_bars = int(input('Select number of bars from Table A-2: '))

  while number_of_bars%4 != 0:
    display('Number of bars has to be a multiple of 4.')
    number_of_bars = int(input('Reselect number of bars from Table A-2: '))

else:

  number_of_bars = int(input('Type number of bars from Table A-2: '))

#This is to determine if the bars can fit in the inner core.
#This inner core size is to determine the core of the column after making an initial selection of the column.
#If the reinforcing does not fit in this smaller area, the column will not work.
#A different bar size and amount of bars must be selected in order to fit in the column
inner_core_size = selected_column_size - 3

display('Core size: ', inner_core_size)
display('Check on Table A-14. Do {} bars fit in the displayed core size area?'.format(number_of_bars))

bar_check = input("Type 'yes' or 'no': ")

count = 0

#This gives the user 5 more attempts to resize their bars before they have to resize the column
#If the user must resize their column, they must select larger values from Table-14
#If they cannot find an adequate size and amount of bars to fit in the column,
#the program will stop working. This is to allow for the user to resize their column.
while bar_check == 'no' and count <= 4:

  count = count + 1

  display('You must reselect a bar size and amount of bars ')

  bar_size = int(input('Reinput bar number: '))

  number_of_bars = int(input('Reinput number of bars: '))

  display('Do {} bars fit in the displayed core size?'.format(number_of_bars))

  bar_check = input("Type 'yes' or 'no': ")


#This kills the program.
#The user has to restart the program from the beginning in order to resize their column.
if count == 5:

  if bar_check == 'no':

    display('You must resize the column core and try again')
    exit()

#Number 3, 4, and 5 bars are used for ties and spiral reinforcement
size_ties = int(input("Input '3', '4', or '5' for size of ties: "))

#The smallest value of the following three checks is used to determine the spacing of the reinforcing ties
#These checks are from the ACI code
if col_type == 'square':

  spacing_one = 16 * (bar_size/8)
  spacing_two = 48 * (size_ties/8)
  spacing_three = selected_column_size

  spacing_ties = min(spacing_one, spacing_two, spacing_three)

#spiral reinforcement are determined differently from ties
elif col_type == 'circular':

  #To determine the spacing of ties, the area of the inner core is required
  #This displays the size of the inner core
  display('From Table A-14, input the area of the {} in core.'.format(inner_core_size))

  #This is the area of the inner core from design Table A-14
  inner_core_area = float(input('Input inner core area from Table A-14: '))

  #Determines the required ratio for the spacing of the spiral
  required_rho = 0.45*((selected_column_area / inner_core_area ) - 1 ) * ( f_conc / f_yield )

  spacing_ties = (4 * ((3.1415 * (size_ties/8)**2) / 4)) / (inner_core_size * required_rho)

  #Rounds the spiral spacing to the nearest quarter inch
  spacing_ties = round(spacing_ties*4)/4

#This last block of code displays all the necessary information required to design the column.
#The first value displayed is the shape of the column

#The second value displayed is the dimension of the column
#This is the length of the sides of a square column
#or the diameter of a circular column.

#The third value displayed is the size of the inner core of the column
#A square column contains a square inner core.
#A circular column contains a circular inner core.

#The fourth value displayed is the size of the reinforcing ties or spirals
#The fifth value displayed is the spacing of these ties or spirals

#The sixth value shown is the amount of reinforcing bars.
#This is the QUANTITY of the bars.

#The last value displayed is the SIZE of the rebars

display('The shape of the column is: {}'.format(col_type),
        'The selected column size is: {} inches.'.format(selected_column_size),
        'The inner core size is: {} inches.'.format(inner_core),
        'The ties are #{} ties'.format(size_ties),
        'with {} inch spacing on center.'.format(spacing_ties),
        'The column contains {}'.format(number_of_bars),
        'size #{} bars.'.format(bar_size)
        )
