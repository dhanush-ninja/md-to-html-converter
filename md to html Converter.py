import markdown
from markdown.extensions.tables import TableExtension
from bs4 import BeautifulSoup

class Converter:
    def __init__(self):
        pass

    def convert_md_to_html(self, markdown_content):
        # Convert Markdown to HTML with table extension
        html_content = markdown.markdown(markdown_content, extensions=['tables', 'attr_list'])

        # Parse the HTML content and convert tables to custom divs
        soup = BeautifulSoup(html_content, 'html.parser')

        # Add Tailwind classes to various elements
        self.add_tailwind_classes(soup)

        # Convert tables to custom divs
        self.convert_tables(soup)

        # Create the full HTML content with JavaScript for play/pause toggle
        full_html_content = self.create_full_html(soup)

        return full_html_content

    def add_tailwind_classes(self, soup):
        for h1 in soup.find_all('h1'):
            h1['class'] = 'text-3xl font-bold mb-4'
        
        for h2 in soup.find_all('h2'):
            h2['class'] = 'text-2xl font-bold mb-4'
        
        for h3 in soup.find_all('h3'):
            h3['class'] = 'text-xl font-bold mb-4'
        
        for p in soup.find_all('p'):
            p['class'] = 'mb-4 text-xl text-justify'
            p['style'] = 'font-family: PT Serif, serif;'
        
        for ul in soup.find_all('ul'):
            ul['class'] = 'list-disc list-inside mb-4 text-justify text-xl'
            ul['style'] = 'font-family: PT Serif, serif;'
        
        for ol in soup.find_all('ol'):
            ol['class'] = 'list-decimal list-inside mb-4 text-justify text-xl'
            ol['style'] = 'font-family: PT Serif, serif;'
        
        for blockquote in soup.find_all('blockquote'):
            blockquote['class'] = 'mb-4 p-4 italic border-l-4 bg-neutral-100 text-neutral-600 border-neutral-500 quote'
            blockquote['style'] = 'font-family: PT Serif, serif;'
        
        for img in soup.find_all('img'):
            img['class'] = 'mx-auto my-4'

    def convert_tables(self, soup):
        for table in soup.find_all('table'):
            divs = []
            rows = table.find_all('tr')
            if len(rows) == 0:
                continue
            
            # Check if the first row is a header
            first_row_cells = rows[0].find_all(['th', 'td'])
            has_headers = len(first_row_cells) == 3 and all(th.name == 'th' for th in first_row_cells)

            start_index = 1 if has_headers else 0

            for row in rows[start_index:]:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:  # Ensure there are at least two cells per row
                    div = soup.new_tag('div', **{'class': 'p-4 my-4 rounded flex items-center justify-center gap-2'})
                    span1 = soup.new_tag('span', **{'class': 'font-bold bg-gray-700 p-4 text-white'})
                    span1.string = cells[0].get_text()
                    span2 = soup.new_tag('span', **{'class': 'font-bold bg-gray-700 p-4 text-white'})
                    span2_content = cells[1].get_text()
                    span2.append(soup.new_string(span2_content))
                    if len(cells) == 3 and cells[2].get_text().strip():
                        audio_button = soup.new_tag('button', **{'class': 'audio-button ml-2', 'data-state': 'play'})
                        audio_button.string = '▶️'
                        audio_url = cells[2].get_text().strip()
                        audio_id = span2_content.lower().replace(' ', '_').replace('[', '').replace(']', '')
                        audio = soup.new_tag('audio', **{'src': audio_url, 'class': 'hidden', 'controls': None})
                        audio_button['onclick'] = f"togglePlayPause('{audio_id}', this);"
                        audio['id'] = audio_id
                        span2.append(audio_button)
                        span2.append(audio)
                    div.append(span1)
                    div.append(span2)
                    divs.append(div)
            table.replace_with(*divs)

    def create_full_html(self, soup):
        return str(soup)

