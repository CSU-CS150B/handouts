## binary
val = bin(255)
print(val) # 0b11111111
val = bin(15)
print(val) # 0b1111
val = bin(136)
print(val) #0b10001000
print(val[2:])
print(int(val, 2))
val = 0b111
print(int(val)) # 7

## strings
barbarian = "conan the barbarian!"
first = barbarian[0:5]
print(first) # conan
no_last = barbarian[:-1]
print(no_last) # conan the barbarian
barb = barbarian[-10:]
print(barb) # barbarian!

sample="Field One:pH=7.2,P2O5=23,K20=5,Ca=40,S=30,Lat=40.5853°N,Lon=105.0844°W;Field Two:K20=6,P2O5=23,pH=7.1,Ca=21,S=30,Lat=40.5852°N,Lon=106.0844°W"

def get_calcium(data, start):
    ca_start = data.find("Ca", start)
    ca_start_num = data.find("=", ca_start) + 1
    ca_end = data.find(",", ca_start)
    return  data[ca_start_num:ca_end]

print(get_calcium(sample,  0)) # 40
print(get_calcium(sample,  sample.find(";"))) # 21

csv = "skeleton,13,12,20".split(",") #['skeleton', '13', '12', '20']
print(csv)

line =  ";".join(csv) #skeleton;13;12;20
print(line)



sample="Field One:pH=7.2,P2O5=23,K20=5,Ca=40,S=30,Lat=40.5853°N,Lon=105.0844°W;" \
       "Field Two:K20=6,P2O5=23,pH=7.1,Ca=21,S=30,Lat=40.5852°N,Lon=106.0844°W"
default_nutrients=["Ca", "S", "K20", "P2O5", "Mg"]

# pull out an element from a field in a sample:
# samples have pattern  <fieldName>:element=value,element=value...;repeats
# post just the value after the =
def get_element(element, field):
    element = element.lower()
    field = field.lower()
    element_location = field.find(element)
    if element_location < 0:
        return None
    start = field.find("=", element_location)+1
    end = field.find(",", start)
    return field[start:end]

# build a card that gives the report, in a nice view by specifications
# loop through each field in the sample (notice pattern of ";")
# loop through each element, within each field, based on elements passed
# return the string that represents - so I know, i am building a string
def build_card(samples, elements):
    analysis_card = "+" + "=" * 28 + "+\n"
    for field in samples.split(";"):
        analysis_card += "|{:<28}|\n".format(field[:field.find(":")])
        for element in elements:
            analysis_card += "|  {:.<16}{:.>10}|\n".format(element,
                                              str(get_element(element, field)))
        analysis_card += "|{}|\n".format("-" * 28)
    analysis_card += "+" + "=" * 28 + "+"
    return analysis_card

def run_analysis():
    response = input("Which nutrients do you want to look at or full report? ").strip()
    elements = default_nutrients if response.upper() == "FULL" else response.split(",")
    print(build_card(sample, elements))

#print("TEST: ",get_element("Ca", sample))

run_analysis()


