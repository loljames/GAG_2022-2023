"""Alchemy."""


class AlchemicalElement:
    """
    AlchemicalElement class.

    Every element must have a name.
    """
    def __init__(self, name: str):
        """AlchemicalElement class constructor."""
        self.name = name
    
    def __repr__(self) -> str:
        """Give name of self."""
        return f"<AE: {self.name}>"


class AlchemicalStorage:
    """AlchemicalStorage class."""

    def __init__(self):
        """
        Initialize the AlchemicalStorage class.

        You will likely need to add something here, maybe a list?
        """
        self.element_list = []

    def add(self, element: AlchemicalElement):
        """
        Add element to storage.

        Check that the element is an instance of AlchemicalElement, if it is not, raise the built-in TypeError exception.

        :param element: Input object to add to storage.
        """
        if isinstance(element, AlchemicalElement):
            self.element_list.append(element)
        else:
            pass

    def pop(self, element_name: str):
        """
        Remove and return previously added element from storage by its name.

        If there are multiple elements with the same name, remove only the one that was added most recently to the
        storage. If there are no elements with the given name, do not remove anything and return None.

        :param element_name: Name of the element to remove.
        :return: The removed AlchemicalElement object or None.
        """
        tempvariable = AlchemicalElement("test")
        for elementIndex in range(1, len(self.element_list)):
            elementIndex = -elementIndex
            if self.element_list[elementIndex].name == element_name and isinstance(self.element_list[elementIndex], AlchemicalElement):
                tempvariable = self.element_list[elementIndex]
                self.element_list.remove(self.element_list[elementIndex])
                return tempvariable
        return None

    def extract(self):
        """
        Return a list of all of the elements from storage and empty the storage itself.

        Order of the list must be the same as the order in which the elements were added.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            storage.extract() # -> [<AE: Water>, <AE: Fire>]
            storage.extract() # -> []

        In this example, the second time we use .extract() the output list is empty because we already extracted everything.

        :return: A list of all of the elements that were previously in the storage.
        """
        new_list = []
        for element in self.element_list:
            new_list.append(element)
        self.element_list.clear()
        return new_list

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the storage.

        Example:
            storage = AlchemicalStorage()
            storage.add(AlchemicalElement('Water'))
            storage.add(AlchemicalElement('Fire'))
            print(storage.get_content())

        Output in console:
            Content:
             * Fire x 1
             * Water x 1

        The elements must be sorted alphabetically by name.

        :return: Content as a string.
        """
        elementdict = {}
        endstring = "Content:"
        if len(self.element_list) > 0: 
            for element in self.element_list:
                #print(len(self.element_list))
                
                #print(element.name in elementdict.keys())
                if element.name in elementdict.keys():
                    print("nohallo.")
                    elementdict[element.name] += 1
                    print(element.name, elementdict[element.name])
                else:
                    elementdict[element.name] = 1
                    print(element.name, elementdict[element.name])
                #print(elementdict)
        
            dict(sorted(elementdict.items()))
            for keyelement in elementdict:
                #print(f"----{keyelement}")
                endstring += f"\n * {keyelement} x {elementdict[keyelement]}"
        else:
            endstring += "\n Empty."
        return endstring


if __name__ == '__main__':
    element_one = AlchemicalElement('Fire')
    element_two = AlchemicalElement('Water')
    element_three = AlchemicalElement('Water')
    storage = AlchemicalStorage()

    #print(element_one)  # <AE: Fire>
    #print(element_two)  # <AE: Water>

    storage.add(element_one)
    storage.add(element_two)
    storage.add(element_three)

    print(storage.get_content())
