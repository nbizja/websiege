import xml.etree.ElementTree as ElementTree

from core.openvas.models.target import Target


class AutoMapper:

    def map_from_xml(self, xml_root: ElementTree, target_class):

        data = self.extract_attributes_from_node(xml_root)

        if target_class == Target.__class__.__name__:
            return Target(data)

        raise


    def extract_attributes_from_node(self, xml_node):
        data = {
            xml_node.tag: {}
        }

        if xml_node.attrib:
            data[xml_node.tag] = xml_node.attrib

        for child_nodes in xml_node:
            data[xml_node.tag].update(self.extract_attributes_from_node(child_nodes))

        return data


