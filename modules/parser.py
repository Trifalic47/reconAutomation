import xml.dom.minidom
import json

filePath = "../output/example_com/example.com.xml"


def parser(filePath=filePath):
    dom = xml.dom.minidom.parse(filePath)

    # Get host element properly
    host = dom.getElementsByTagName("host")[0]

    # Extract IP
    address = host.getElementsByTagName("address")[0]
    ip = address.getAttribute("addr")

    # Extract Hostname
    hostnames = host.getElementsByTagName("hostnames")[0]
    hostname = hostnames.getElementsByTagName("hostname")[0]
    name = hostname.getAttribute("name")

    # Prepare result structure
    result = {"ip": ip, "hostname": name, "ports": []}

    # Extract open ports
    ports = host.getElementsByTagName("port")

    for port in ports:
        state = port.getElementsByTagName("state")[0].getAttribute("state")

        if state == "open":
            portid = port.getAttribute("portid")
            protocol = port.getAttribute("protocol")

            service = port.getElementsByTagName("service")[0]
            service_name = service.getAttribute("name")
            product = service.getAttribute("product")

            port_data = {
                "port": int(portid),
                "protocol": protocol,
                "service": service_name,
                "product": product,
            }

            result["ports"].append(port_data)

    return result


if __name__ == "__main__":
    data = parser()
    print(json.dumps(data, indent=4))
