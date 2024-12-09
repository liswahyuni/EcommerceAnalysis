import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import base64
import os


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
    
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Read the CSV files
    segment_analysis = pd.read_csv(os.path.join(current_dir, 'segment_analysis.csv'))
    rfm_df = pd.read_csv(os.path.join(current_dir, 'rfm_df.csv'))
    segment_distribution = pd.read_csv(os.path.join(current_dir, 'segment_distribution.csv'))
    
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
        
        st.write("""
        ### Purchasing Patterns Based on Recency, Frequency, and Monetary
        - Recency (as shown in the first graph) indicates that customers who make purchases more frequently (such as segments like Big Spenders and Loyal Customers) tend to have lower recency values, meaning they have recently made transactions. This is an indicator that they are active customers with high potential for retention.
        - Frequency (second graph) shows that customers who transact more often are typically found in segments such as Champions, Loyal Customers, Lost Loyal, and Lost Champions. Customers in these segments have higher purchase frequencies, reflecting their loyalty to the brand or product.
        - Monetary (third graph) highlights that the Champions and Big Spenders segments have higher total spending, indicating that these customers contribute the most to the company's revenue. Meanwhile, Lost Customers and Recent Customers tend to spend less.         
            """)

        st.write("""
        ### Implications for Pricing Strategy
        - Discount Strategy for Recent Customers and Lost Customers: Customers who have recently made purchases or have lost interest (like Recent Customers and Lost Customers) may be more price-sensitive. Offering discounts or special promotions can help attract them back, encourage more purchases, and extend their customer lifecycle.
        - Premium Pricing for Champions: For proven big spenders and loyal customers (like Champions), a premium pricing strategy (where products or services are priced higher than similar items in the market to create a perception of higher value) could be implemented. These customers are likely to value product quality over price and may tolerate higher prices more readily.
        - Retention for High Recency Segments: Loyal customers with frequent transactions could be incentivized through loyalty programs or competitive pricing, coupled with enhanced services, to retain them for longer periods.
        """)         
    
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

        st.write("""
        ### Correlation Analysis
        The correlation analysis shows the correlation between RFM metrics:
        - Spearman's correlation is used to measure the strength of the relationship between two variables.
        - The higher the correlation, the stronger the relationship.
        - The correlation coefficient ranges from -1 to 1, with 1 representing a perfect positive correlation, -1 representing a perfect negative correlation, and 0 representing no correlation.
        """)

        st.write("""
        ### RFM Relationship Across Segments
        - Recency vs Frequency:
        Champions and Loyal Customers tend to have high frequency.
        Lost Big Spenders and Lost Customers show lower frequency, indicating inactivity.
        - Recency vs Monetary:
        Champions and Big Spenders tend to have high monetary values, indicating frequent large purchases.
        - Frequency vs Monetary:
        Segments like Champions and Big Spenders exhibit both high frequency and high monetary values.
        """)

        st.write("""
        ### Suggestions for Pricing Strategy
        - Customers who frequently transact and have high spending contribute significantly to revenue and should be retained through premium pricing strategies and loyalty programs.
        - New or inactive customers should be given attention through more attractive pricing approaches, such as discounts or special offers, to encourage them to make purchases more frequently.
        - Flexible and segmentation-based pricing strategies are essential to maximize revenue and retain high-value customers.     
        """)

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

        st.write("""
        ### Implications for Pricing Strategy
        a) **Strategy for Mid-Value Segment (59.92%):**  
        - Maintain a pricing "sweet spot" around Rp 99.99 (median).  
        - Implement bundling programs to encourage purchases in the Rp 100,000 - 150,000 range.  
        - Create loyalty programs with rewards around the median value to promote repeat purchases.  
        - Focus on a strong value proposition to maintain the dominance of this segment.  

        b) **Strategy for Low-Value Segment (29.91%):**  
        - Apply "price anchoring" by showcasing mid-value products as comparisons.  
        - Create bundled packages with psychological pricing (e.g., Rp 49.99) to encourage upgrades to mid-value.  
        - Offer free shipping incentives for purchases over Rp 50,000.  
        - Focus on purchase volume and frequency to compensate for smaller margins.  

        c) **Strategy for High-Value Segment (10.18%):**  
        - Develop premium product lines with higher margins.  
        - Offer exclusive services (e.g., priority shipping, dedicated customer support).  
        - Implement dynamic pricing for premium products.  
        - Create an exclusive membership program with special benefits.  

        ### Recommendations

        a) **Pricing Optimization:**  
        - Set psychological pricing around Rp 99.99 for mid-value products.  
        - Establish clear pricing tiers: < Rp 50,000, Rp 50,000-200,000, > Rp 200,000.  
        - Apply surge pricing during peak demand periods.  

        b) **Loyalty Programs:**  
        - Design rewards based on transaction value tiers.  
        - Provide incentives for upgrading to higher tiers.  
        - Introduce milestone rewards to encourage higher transaction values.  

        c) **Promotion Strategy:**  
        - Align promotion types with the characteristics of each segment.  
        - Focus on value upgrades for the low-value segment.  
        - Offer exclusive early access for the high-value segment.  
        """)

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