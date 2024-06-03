### TYPE_HINTS ###



###                  ESTO NOS DICE QUE ES TIPO DINAMICO                                                  ###
my_string_variable = "my String variable"

print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 123
print(my_string_variable)
print(type(my_string_variable))
print('//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')




### FastAPI nos pide que especificando el tipo de la variable ###
my_typed_variable: str = "My Typed String variable"
print(my_typed_variable)
print(type(my_typed_variable))

my_typed_variable = 5
print(my_typed_variable)
print(type(my_typed_variable))