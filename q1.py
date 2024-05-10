recurrence_dict = {
'current_location': 'Usa',
'job': 'sofware engineer',
'older_location': 'Canada'
}
print("Before popping: ", recurrence_dict)
# Lets remove the last item
recurrence_dict.popitem()#list.pop = it removes and returns the last element of the list
print("After popping: ", recurrence_dict)#dict.pop =  removes elements from a dictionary by key.
