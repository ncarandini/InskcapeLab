import inkex

class ListCenterCoordinates(inkex.Effect):
    def process_element(self, elem):
        if elem.tag == inkex.addNS('circle', 'svg'):  # Check if the element is a circle
            # Get the raw cx, cy, and r attributes
            cx = float(elem.get('cx', 0))
            cy = float(elem.get('cy', 0))
            r = float(elem.get('r', 0))

            # Retrieve the ID and label of the element
            elem_id = elem.get('id')  # Retrieve the ID of the element
            label = elem.get(inkex.addNS('label', 'inkscape'), 'No Label')  # Retrieve the label

            # Debug output
            inkex.debug("Circle ID: {} - Label: '{}' - Center: ({}, {}) - Radius: {}".format(label, elem_id, cx, cy, r))
            
        elif elem.tag == inkex.addNS('g', 'svg'):  # Check if the element is a group
            # Loop through child elements
            for child in elem:
                self.process_element(child)
        else:
            # Message for elements that are neither circles nor groups
            elem_id = elem.get('id', 'Unknown ID')
            inkex.debug("Element ID: {} is not a circle or a group and will be skipped.".format(elem_id))

    def effect(self):
        for elem in self.selected.values():
            self.process_element(elem)

if __name__ == '__main__':
    ListCenterCoordinates().affect()



