import re

class URLConnectorParser(object):
    def parse_URL(self, url):
        pattern = re.compile(r'''
            (?P<name>[\w\+]+)://
            (?:
                (?P<username>[^:/]*)
                (?::(?P<password>.*))?
            @)?
            (?:
                (?:
                    \[(?P<ipv6host>[^/]+)\] |
                    (?P<ipv4host>[^/:]+)
                )?
                (?::(?P<port>[^/]*))?
            )?
            (?:/(?P<database>.*))?
            ''', re.X)
        match = pattern.match(url)
        if match is not None:
            components = match.groupdict()
            return components

    def process_url(self, connector, url):
        connector.set_connection_data(self.parse_URL(url))