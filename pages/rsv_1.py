from st_pages import add_page_title
from utils.constants import rsv_file_names, rsv_page_names, rsv_descriptions, rsv_url
from utils.css_utils import display_download_button
from utils.text_utils import display_data_description, display_source
from utils.visualization_utils import univariate_distribution, multivariate_distribution, display_dataset

key = "rsv_1"
file_name = rsv_file_names[key]

add_page_title(page_title=rsv_page_names[key], layout="wide")

display_data_description(rsv_descriptions[key])
display_source(rsv_url[key])

display_download_button(file_name)

#univariate_distribution(file_name)
#multivariate_distribution(file_name)
display_dataset(file_name)


