### Drawing a Graph from a Website

This project involves fetching data from a website and visualizing it in the form of graphs using Python. The code retrieves performance data for various entities (e.g., investment platforms, financial tools, etc.) from a web source, processes the data, and generates line graphs to represent the performance trends over time. The graphs are saved as image files for further use or analysis.

#### Key Features:
1. Data Retrieval: The script uses the requests library to fetch data from a specified website or API endpoint. The data is expected to be in a structured format (e.g., JSON) containing labels (e.g., dates) and corresponding performance metrics.

2. Data Visualization: The matplotlib library is used to create line graphs. Each graph plots the performance data against time (dates) and includes a title, axis labels, and a legend for clarity.

3. Dynamic Graph Generation: The script iterates through a dictionary of entities (e.g., "whitebox", "quirion", "bevestor", etc.), extracting relevant data for each entity and generating a separate graph. This allows for scalable and automated visualization of multiple datasets.

4. Customization: The graphs are customized with specific colors, markers, grid lines, and font sizes to enhance readability. The x-axis labels (dates) are rotated for better visibility, and the graphs are saved as high-quality PNG images.

5. Output: Each graph is saved as a separate image file named after the corresponding entity (e.g., "whitebox.png", "quirion.png", etc.). The images can be used for reports, presentations, or further analysis.

#### Example Use Case:
This project could be used in financial analysis to visualize the performance of various investment platforms over time. By plotting the data, users can easily identify trends, compare performance, and make informed decisions.

#### Code Overview:
- Data Fetching: The requests.get() function retrieves data from the website or API.
- Data Processing: The script extracts labels (dates), performance data, titles, and labels from the fetched data.
- Graph Plotting: The matplotlib.pyplot library is used to create and customize the line graphs.
- Saving Graphs: Each graph is saved as a PNG file using plt.savefig().

#### Example Output:
For each entity in the items dictionary, a graph is generated and saved. For instance, the graph for "whitebox" will show its performance over time, with dates on the x-axis and performance percentages on the y-axis. The graph will include a title, axis labels, and a legend for context.

#### Libraries Used:
- requests: For fetching data from the web.
- matplotlib.pyplot: For creating and customizing graphs.

#### Future Enhancements:
- Add error handling for failed data fetches.
- Support for additional graph types (e.g., bar charts, scatter plots).
- Integration with databases or cloud storage for automated data retrieval and graph storage.
- Interactive graphs using libraries like Plotly for web-based dashboards.
