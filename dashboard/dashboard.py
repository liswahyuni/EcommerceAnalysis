import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import base64

def main():
    st.markdown(
        "<h1 style='text-align: center;'>Customer Segmentation Dashboard</h1>",
        unsafe_allow_html=True
    )
    
    # Add RFM diagram SVG
    svg_content = '''
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500">
    <!-- Background -->
    <rect width="800" height="500" fill="#f8fafc" />
    
    <!-- Title -->
    <text x="400" y="50" text-anchor="middle" font-size="24" font-weight="bold" fill="#1e293b">
        RFM Customer Segmentation
    </text>

    <!-- Main Circles -->
    <g transform="translate(400, 250)">
        <!-- Recency Circle -->
        <circle cx="-150" cy="-50" r="80" fill="#60a5fa" fill-opacity="0.8" />
        <text x="-150" y="-50" text-anchor="middle" fill="white" font-size="20" font-weight="bold">Recency</text>
        <text x="-150" y="-30" text-anchor="middle" fill="white" font-size="12">
            Last Purchase
        </text>
        <text x="-150" y="-10" text-anchor="middle" fill="white" font-size="12">
            Time
        </text>

        <!-- Frequency Circle -->
        <circle cx="0" cy="-50" r="80" fill="#34d399" fill-opacity="0.8" />
        <text x="0" y="-50" text-anchor="middle" fill="white" font-size="20" font-weight="bold">Frequency</text>
        <text x="0" y="-30" text-anchor="middle" fill="white" font-size="12">
            Number of
        </text>
        <text x="0" y="-10" text-anchor="middle" fill="white" font-size="12">
            Purchases
        </text>

        <!-- Monetary Circle -->
        <circle cx="150" cy="-50" r="80" fill="#f472b6" fill-opacity="0.8" />
        <text x="150" y="-50" text-anchor="middle" fill="white" font-size="20" font-weight="bold">Monetary</text>
        <text x="150" y="-30" text-anchor="middle" fill="white" font-size="12">
            Total Spend
        </text>
        <text x="150" y="-10" text-anchor="middle" fill="white" font-size="12">
            Amount
        </text>

        <!-- Connecting Lines -->
        <path d="M-70,-50 L-80,-50" stroke="#94a3b8" stroke-width="2" />
        <path d="M80,-50 L70,-50" stroke="#94a3b8" stroke-width="2" />

        <!-- Customer Segments Box -->
        <rect x="-200" y="50" width="400" height="180" rx="10" fill="#1e293b" />
        <text x="0" y="80" text-anchor="middle" fill="white" font-size="18" font-weight="bold">Customer Segments</text>
        <text x="-180" y="110" fill="white" font-size="14">• Big Spenders</text>
        <text x="-180" y="135" fill="white" font-size="14">• Champions</text>
        <text x="-180" y="160" fill="white" font-size="14">• Lost Big Spenders</text>
        <text x="-180" y="185" fill="white" font-size="14">• Lost Champions</text>
        <text x="20" y="110" fill="white" font-size="14">• Lost Customers</text>
        <text x="20" y="135" fill="white" font-size="14">• Lost Loyal</text>
        <text x="20" y="160" fill="white" font-size="14">• Loyal Customers</text>
        <text x="20" y="185" fill="white" font-size="14">• Recent Customers</text>
    </g>

    <!-- Decorative Elements -->
    <circle cx="50" cy="50" r="20" fill="#60a5fa" fill-opacity="0.3" />
    <circle cx="750" cy="450" r="25" fill="#34d399" fill-opacity="0.3" />
    <circle cx="700" cy="80" r="15" fill="#f472b6" fill-opacity="0.3" />
    <circle cx="100" cy="400" r="18" fill="#60a5fa" fill-opacity="0.3" />
</svg>
    </svg>
    '''
    
    # Convert SVG to base64
    b64 = base64.b64encode(svg_content.encode('utf-8')).decode()
    
    # Display the SVG using HTML
    st.markdown(
        f'<div style="display: flex; justify-content: center; margin-bottom: 2rem;">'
        f'<img src="data:image/svg+xml;base64,{b64}" style="width: 800px; max-width: 100%;">'
        f'</div>',
        unsafe_allow_html=True
    )
    
    # Add copyright notice outside the image
    st.markdown(
        '<div style="text-align: center; color: #666; margin-bottom: 2rem;">'
        '© 2024 by Lis Wahyuni'
        '</div>',
        unsafe_allow_html=True
    )
    
    st.write("""
    This dashboard provides an overview of customer segmentation and transaction analysis using a combination of RFM (Recency, Frequency, Monetary) analysis and value-based clustering. By analyzing transactional data, the dashboard categorizes customers into actionable segments, helping businesses tailor their marketing strategies and optimize customer engagement.
    """)
    
    # Load your data
    segment_analysis = pd.read_csv('/workspaces/EcommerceAnalysis/dashboard/segment_analysis.csv')
    rfm_df = pd.read_csv('/workspaces/EcommerceAnalysis/dashboard/rfm_df.csv')
    segment_distribution = pd.read_csv('/workspaces/EcommerceAnalysis/dashboard/segment_distribution.csv')
    
    # Create tabs for different visualizations
    tab1, tab2, tab3, tab4 = st.tabs(["Distribution Analysis", "Segment Comparison", "Metric Relationships", "Clustering"])

    with tab1:
        st.write("""
        ### Distribution Analysis
        These box plots show how RFM metrics are distributed across different customer segments.
        - **Outliers** are shown as individual points
        - **Box** represents the interquartile range (IQR)
        - **Line** in the box represents the median
        """)
        create_distribution_plots(rfm_df)

    with tab2:
        st.write("""
        ### Segment Comparison
        Compare average RFM metrics across different customer segments to understand their characteristics.
        - Bars show the median value for each metric
        - Higher values indicate better performance (except for recency)
        """)
        create_segment_comparison(segment_analysis)
    
    with tab3:
        st.write("""
        ### Metric Relationships
        The scatter matrix shows relationships between RFM metrics:
        - Each point represents a customer
        - Colors indicate different segments
        - Diagonal shows distribution of each metric
        - Correlations help understand metric relationships
        """)
        create_scatter_matrix(rfm_df)

    with tab4:
        st.write("""
        ### Clustering Explanation
Clustering Logic: The clustering process categorizes transactions into three distinct value-based segments based on the transaction value:

1. Low-Value Segment (< 50): This segment represents customers with low transaction amounts. They may be occasional or less engaged buyers.

2. Mid-Value Segment (50 to 200): These customers make moderate-value purchases, representing a stable and reliable customer base.

3. High-Value Segment (> 200): These are premium customers contributing the highest transaction amounts. They are likely highly engaged and valuable to the business.
        """)
    
        # Generate and display the donut chart
        fig = plot_donut_plotly(segment_distribution)
        st.plotly_chart(fig, use_container_width=True)


# Function to prepare segment data for comparison
def prepare_segment_data(segment_analysis):
    """Convert segment_analysis from long to wide format for easier plotting"""
    # Reset index to make Segment and Metric regular columns
    df = segment_analysis.reset_index()
    
    # Now perform the pivot
    wide_df = df.pivot(
        index='Segment', 
        columns='Metric', 
        values=['Mean', 'Median', 'Distribution']
    ).reset_index()
    
    # Flatten column names
    wide_df.columns = [f'{col[0]}_{col[1]}'.strip() if col[1] else col[0] 
                      for col in wide_df.columns]
    
    return wide_df

def create_distribution_plots(rfm_df, metrics=['recency', 'frequency', 'monetary']):
    """Create box plots for multiple metrics"""
    for metric in metrics:
        st.subheader(f'Distribution of {metric.capitalize()} by Customer Segment')
        
        fig = px.box(
            rfm_df,
            x='Customer_Segment',
            y=metric,
            color='Customer_Segment',
            notched=True,
            points="outliers"  # Only show outlier points
        )
        fig.update_layout(
            showlegend=False,
            xaxis_title='Customer Segment',
            yaxis_title=metric.capitalize(),
            height=500,
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Add descriptive statistics
        st.write(f"Key Statistics for {metric.capitalize()}:")
        stats = rfm_df.groupby('Customer_Segment')[metric].agg(['mean', 'median', 'std']).round(2)
        st.dataframe(stats)

def create_segment_comparison(segment_analysis):
    """Create subplot comparing metrics across segments"""
    st.subheader('Comparison of RFM Metrics Across Segments')
    
    wide_segment = prepare_segment_data(segment_analysis)
    metrics = ['recency', 'frequency', 'monetary']
    
    fig = make_subplots(
        rows=1, cols=3,
        subplot_titles=[f'{m.capitalize()} by Segment' for m in metrics]
    )
    
    for i, metric in enumerate(metrics, 1):
        median_col = f'Median_{metric}'
        fig.add_trace(
            go.Bar(
                x=wide_segment['Segment'],
                y=wide_segment[median_col],
                name=f'Median {metric.capitalize()}',
                text=wide_segment[median_col].round(2),
                textposition='auto',
            ),
            row=1, col=i
        )
        
        fig.update_xaxes(tickangle=-45, row=1, col=i)
    
    fig.update_layout(
        height=600,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Add insights
    st.write("Key Insights:")
    for metric in metrics:
        best_segment = wide_segment.loc[wide_segment[f'Median_{metric}'].idxmax()]
        st.write(f"- Highest {metric}: {best_segment['Segment']} segment with median {best_segment[f'Median_{metric}']:.2f}")

def create_scatter_matrix(rfm_df):
    """Create scatter matrix for RFM metrics"""
    st.subheader('RFM Metrics Relationships')
    
    fig = px.scatter_matrix(
        rfm_df,
        dimensions=['recency', 'frequency', 'monetary'],
        color='Customer_Segment',
        title='RFM Metrics Relationships'
    )
    fig.update_layout(height=800)
    st.plotly_chart(fig, use_container_width=True)
    
    # Add correlation analysis
    st.write("Correlation Analysis:")
    corr = rfm_df[['recency', 'frequency', 'monetary']].corr(method='spearman').round(3)
    st.dataframe(corr)

# Function to create a Plotly donut chart
def plot_donut_plotly(segment_distribution):
    # Extract values and labels from the DataFrame
    labels = segment_distribution['segment']
    values = segment_distribution['proportion']
    
    # Define custom colors
    colors = ['#f2e394', '#f7d0a1', '#f1a7a9']
    
    # Create the donut chart
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.5,  # Creates the donut hole
        textinfo='percent+label',  # Shows percentage and labels
        marker=dict(colors=colors),  # Custom colors
        textfont=dict(size=12),
    )])
    
    # Update layout for title and style
    fig.update_layout(
        title='Transaction Value Distribution',
        title_x=0.5,  # Center the title
        title_font=dict(size=18),
        showlegend=True
    )
    return fig


if __name__ == "__main__":
    main()