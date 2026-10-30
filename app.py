import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from sqlalchemy import create_engine
import mysql.connector

mydb = mysql.connector.connect(
    host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
    user="3Yf68YwHaZosnho.root",
    password="AMFwYtGzLCZGJ9Td",
    database="TMDB"
)

df_movies = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_movies.csv")
df_cast = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\cleaned_cast.csv")
df_crew = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_crew.csv")
df_genres = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_genres.csv")
df_movie_genres = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_movie_genres.csv")
df_movie_keywords = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_movie_keywords.csv")

if mydb.is_connected():
    print("MySQL Connected Successfully!")

engine = create_engine(
    "mysql+pymysql://3Yf68YwHaZosnho.root:AMFwYtGzLCZGJ9Td@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/TMDB"
)

df_cast.to_sql(
    name="casting",
    con=engine,
    if_exists="replace",
    index=False
)

print("CSV loaded into MySQL successfully!")   


engine = create_engine(
    "mysql+pymysql://3Yf68YwHaZosnho.root:AMFwYtGzLCZGJ9Td@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/TMDB"
)

df_crew.to_sql(
    name="crewing",
    con=engine,
    if_exists="replace",
    index=False
)

print("CSV loaded into MySQL successfully!")


engine = create_engine(
    "mysql+pymysql://3Yf68YwHaZosnho.root:AMFwYtGzLCZGJ9Td@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/TMDB"
)

df_genres.to_sql(
    name="genres",
    con=engine,
    if_exists="replace",
    index=False
)

print("CSV loaded into MySQL successfully!")


engine = create_engine(
    "mysql+pymysql://3Yf68YwHaZosnho.root:AMFwYtGzLCZGJ9Td@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/TMDB"
)

df_movie_genres.to_sql(
    name="movie_genres",
    con=engine,
    if_exists="replace",
    index=False
)

print("CSV loaded into MySQL successfully!")


engine = create_engine(
    "mysql+pymysql://3Yf68YwHaZosnho.root:AMFwYtGzLCZGJ9Td@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/TMDB"
)

df_movie_keywords.to_sql(
    name="movie_keywords",
    con=engine,
    if_exists="replace",
    index=False
)

print("CSV loaded into MySQL successfully!")


engine = create_engine(
    "mysql+pymysql://3Yf68YwHaZosnho.root:AMFwYtGzLCZGJ9Td@gateway01.ap-southeast-1.prod.aws.tidbcloud.com/TMDB"
)

df_movies.to_sql(
    name="movies",
    con=engine,
    if_exists="replace",
    index=False
)

print("CSV loaded into MySQL successfully!")




st.set_page_config(
    page_title="TMDB Movie Analytics",
    page_icon="🎬",
    layout="wide"
)

st.title("TMDB Movie Analytics")

df_movies = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_movies.csv")
df_cast = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\cleaned_cast.csv")
df_crew = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_crew.csv")
df_genres = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_genres.csv")
df_movie_genres = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_movie_genres.csv")
df_movie_keywords = pd.read_csv("D:\GUVI\Project\Datasets\data\clean data\Cleaned_movie_keywords.csv")

st.sidebar.title("🎬 TMDB Analytics")

with st.sidebar:
    selected = option_menu("", ["Home","Filters","Dashboard",'Queries'], 
        icons=['house',"sliders","bar-chart","search"], default_index=1)

if selected == "Home":

    st.markdown("""
    <style>
    .hero {
        padding: 45px 30px;
        border-radius: 18px;
        background: linear-gradient(120deg, #071b2b, #123c52, #80552a);
        color: white;
        text-align: center;
        border: 1px solid #31536a;
    }
    .hero h1 {
        font-size: 42px;
        margin-bottom: 12px;
    }
    .hero p {
        font-size: 18px;
        color: #e0eaf0;
    }
    .info-card {
        background: #102638;
        color: white;
        padding: 22px;
        border-radius: 14px;
        min-height: 155px;
        border: 1px solid #29465b;
    }
    .info-card h3 {
        color: #f5bd65;
    }
    </style>

    <div class="hero">
        <h1>🎬 TMDB Movie Analytics</h1>
        <p>Discover the stories behind the movies through data.</p>
        <p>Explore movies, genres, actors, crew and cinematic trends.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.subheader("Welcome to the Movie Analytics Hub")

    st.write(
        "This project uses six cleaned datasets to explore "
        "movie performance, genres, cast, crew and keywords "
        "through interactive visualizations and analytical queries."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🎞️ Movie Insights</h3>
            <p>Explore release years, budgets, revenue,
            popularity and ratings.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🎭 Genres & Cast</h3>
            <p>Discover genre patterns, actors and
            movie collaborations.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card">
            <h3>📊 Data Analytics</h3>
            <p>Understand movie trends through
            interactive Plotly charts and queries.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Explore the Application")

    st.markdown("""
    - **Filters:** Narrow down movies using your selected criteria.
    - **Dashboard:** Explore interactive charts and visual insights.
    - **Queries:** Select an analytical question and view its answer.
    """)

    st.info(
        "Start with Filters, explore the Dashboard, "
        "and use Query Explorer to discover movie insights."
    )

elif selected == "Filters":

    st.title("🎬 Movie Filters")
    st.write("Select filters below to explore matching movies.")

    
    st.subheader("📅 Release Year")

    df_movies["year"] = pd.to_numeric(
        df_movies["year"], errors="coerce"
    )

    years = sorted(
        df_movies["year"].dropna().astype(int).unique().tolist()
    )

    selected_years = st.multiselect(
        "Choose year(s)",
        options=years,
        default=[],
        key="filter_years"
    )

   
    st.subheader("🎭 Genre")

    genre_data = df_movie_genres.merge(
        df_genres,
        on="genre_id",
        how="left"
    )

    genre_names = sorted(
        genre_data["genre_name"].dropna().unique().tolist()
    )

    selected_genres = st.multiselect(
        "Choose genre(s)",
        options=genre_names,
        default=[],
        key="filter_genres"
    )

    
    st.subheader("🌐 Original Language")

    languages = sorted(
        df_movies["original_language"].dropna().unique().tolist()
    )

    selected_languages = st.multiselect(
        "Choose language(s)",
        options=languages,
        default=[],
        key="filter_languages"
    )

   
    st.subheader("⭐ Minimum Rating")

    min_rating = st.slider(
        "Select minimum rating",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.5,
        key="filter_min_rating"
    )

    filtered_movies = df_movies.copy()

    if selected_years:
        filtered_movies = filtered_movies[
            filtered_movies["year"].isin(selected_years)
        ]

    if selected_genres:
        matching_movie_ids = genre_data[
            genre_data["genre_name"].isin(selected_genres)
        ]["movie_id"].unique()

        filtered_movies = filtered_movies[
            filtered_movies["movie_id"].isin(matching_movie_ids)
        ]

    if selected_languages:
        filtered_movies = filtered_movies[
            filtered_movies["original_language"].isin(
                selected_languages
            )
        ]

    filtered_movies = filtered_movies[
        filtered_movies["vote_average"].fillna(0) >= min_rating
    ]

    
    st.divider()

    st.subheader("🎥 Filtered Movies")
    st.metric("Movies Found", len(filtered_movies))

    st.dataframe(
        filtered_movies,
        use_container_width=True
    )


elif selected == "Dashboard":


    st.title("🎬 TMDB Movie Analytics Dashboard")
    st.write("Explore your selected movies using KPIs and charts and full visualizations")

    # 1. Read filter selections
    selected_years = st.session_state.get("filter_years", [])
    selected_genres = st.session_state.get("filter_genres", [])
    selected_languages = st.session_state.get("filter_languages", [])
    min_rating = st.session_state.get("filter_min_rating", 0.0)

    # 2. Apply the filters to movies
    dashboard_movies = df_movies.copy()

    if selected_years:
        dashboard_movies = dashboard_movies[
            dashboard_movies["year"].isin(selected_years)
        ]

    if selected_genres:
        genre_map = df_movie_genres.merge(
            df_genres,
            on="genre_id",
            how="left"
        )

        matching_ids = genre_map[
            genre_map["genre_name"].isin(selected_genres)
        ]["movie_id"].unique()

        dashboard_movies = dashboard_movies[
            dashboard_movies["movie_id"].isin(matching_ids)
        ]

    if selected_languages:
        dashboard_movies = dashboard_movies[
            dashboard_movies["original_language"].isin(
                selected_languages
            )
        ]

    dashboard_movies = dashboard_movies[
        dashboard_movies["vote_average"].fillna(0) >= min_rating
    ]

    # IDs of the currently filtered movies
    movie_ids = dashboard_movies["movie_id"].unique()

    # 3. Prepare related data for these movies
    dashboard_genres = df_movie_genres[
        df_movie_genres["movie_id"].isin(movie_ids)
    ].merge(
        df_genres,
        on="genre_id",
        how="left"
    )

    dashboard_cast = df_cast[
        df_cast["movie_id"].isin(movie_ids)
    ]

    # 4. KPI cards - first row
    total_movies = dashboard_movies["movie_id"].nunique()
    total_genres = dashboard_genres["genre_id"].nunique()
    total_actors = dashboard_cast["person_id"].nunique()
    average_rating = dashboard_movies["vote_average"].mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🎬 Total Movies", f"{total_movies:,}")

    with col2:
        st.metric("🎭 Total Genres", f"{total_genres:,}")

    with col3:
        st.metric("🎭 Total Actors", f"{total_actors:,}")

    with col4:
        if pd.notna(average_rating):
            st.metric("⭐ Average Rating", f"{average_rating:.2f}/10")
        else:
            st.metric("⭐ Average Rating", "N/A")

    st.divider()

    # 5. Chart 1 - Top 10 movies by revenue
    st.subheader("💰 Top 10 Movies by Revenue")

    revenue_data = dashboard_movies.dropna(
        subset=["revenue", "title"]
    )

    top_movies = revenue_data[
        revenue_data["revenue"] > 0
    ].nlargest(10, "revenue")

    # Two-column layout starts here
    left_col, right_col = st.columns(2)

    with left_col:
        if not top_movies.empty:
            fig_revenue = px.bar(
                top_movies.sort_values("revenue"),
                x="revenue",
                y="title",
                orientation="h",
                title="Top 10 Movies by Revenue",
                labels={
                    "revenue": "Revenue",
                    "title": "Movie"
                }
            )

            st.plotly_chart(
                fig_revenue,
                use_container_width=True
            )
        else:
            st.info("No valid revenue data for this selection.")

    # 6. Chart 2 - Genre distribution
    with right_col:
        st.subheader("🎭 Genre Distribution")

        genre_counts = (
            dashboard_genres.groupby("genre_name")["movie_id"]
            .nunique()
            .reset_index(name="movie_count")
            .sort_values("movie_count", ascending=False)
        )

        if not genre_counts.empty:
            fig_genres = px.pie(
                genre_counts,
                names="genre_name",
                values="movie_count",
                hole=0.45,
                title="Movies by Genre"
            )

            st.plotly_chart(
                fig_genres,
                use_container_width=True
            )
        else:
            st.info("No genre data for this selection.")

    st.divider()

    # 7. Chart 3 - Budget vs Revenue
    st.subheader("📈 Budget vs Revenue")

    scatter_data = dashboard_movies.dropna(
        subset=["budget", "revenue", "title"]
    )

    scatter_data = scatter_data[
        (scatter_data["budget"] > 0) &
        (scatter_data["revenue"] > 0)
    ]

    if not scatter_data.empty:
        fig_scatter = px.scatter(
            scatter_data,
            x="budget",
            y="revenue",
            hover_name="title",
            color="original_language",
            title="Movie Budget vs Revenue",
            labels={
                "budget": "Budget",
                "revenue": "Revenue",
                "original_language": "Language"
            }
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )
    else:
        st.info("No valid budget and revenue values for this selection.")

    st.divider()

    # 8. Text insight - highest grossing genre
    st.subheader("💡 Key Insight")

    revenue_by_genre = dashboard_genres.merge(
        dashboard_movies[["movie_id", "revenue"]],
        on="movie_id",
        how="left"
    )

    revenue_by_genre = revenue_by_genre.dropna(
        subset=["genre_name", "revenue"]
    )

    revenue_by_genre = revenue_by_genre[
        revenue_by_genre["revenue"] > 0
    ]

    genre_revenue = (
        revenue_by_genre.groupby("genre_name")["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    if not genre_revenue.empty:
        highest_genre = genre_revenue.index[0]
        highest_revenue = genre_revenue.iloc[0]

        st.success(
            f"Highest-grossing genre in this selection is "
            f"{highest_genre}, with total revenue of "
            f"{highest_revenue:,.0f}."
        )
    else:
        st.info("Not enough valid revenue data to identify the top genre.")
    

    
    st.subheader("📊 VISUALIZATION 1")

    st.write("INSIGHTS - after the year of 2000 lot of files are released")
    
    df_year = df_movies.groupby("year")["movie_id"].nunique().reset_index()

    fig = px.line(
    df_year,
    x="year",
    y="movie_id",
    title="Number of Movies Released Each Year"
   )

    st.plotly_chart(fig, use_container_width=True)   

    st.divider()
    st.subheader("📊 VISUALIZATION 2")

    st.write("INSIGHTS - Almost all movie vote_average will be around 6 to 8")

    df_primary_genre = (
    df_movie_genres
    .drop_duplicates(subset="movie_id", keep="first")
    .merge(df_genres, on="genre_id", how="left")
    [["movie_id", "genre_name"]]
    .rename(columns={"genre_name": "primary_genre"})
    )

    df_pairplot = df_movies.merge(
    df_primary_genre,
    on="movie_id",
    how="left"
    )

    cols = [
    "budget",
    "revenue",
    "popularity",
    "vote_average",
    "primary_genre"
    ]

    df_pairplot = df_pairplot[cols].dropna()

    fig = px.scatter_matrix(
    df_pairplot,
    dimensions=[
        "budget",
        "revenue",
        "popularity",
        "vote_average"
    ],
    color="primary_genre",
    title="Movie Pairplot by Primary Genre",
    opacity=0.5
    )

    fig.update_traces(
    diagonal_visible=True,
    showupperhalf=False,
    marker=dict(size=5)
    )


    st.plotly_chart(fig, use_container_width=True)


    st.divider()
    st.subheader("📊 VISUALIZATION 3")

    st.write("INSIGHTS - Most of the films budget is around 1 to 50 million")

    df_budget=df_movies[df_movies["budget"] > 0]

    fig = px.histogram(
    df_budget,
    x="budget",
    nbins=50,
    title="Distribution of movie budget"
    )

    st.plotly_chart(fig, use_container_width=True)


    st.divider()
    st.subheader("📊 VISUALIZATION 4")

    st.write("INSIGHTS")
    st.write("Typical movie runtime 111 minutes")
    st.write("50% movie are in between the runtime of 99 to 126 minutes")
    st.write("Longest movie in the dataset will be 242 minutes")
    st.write("shortest movie in the dataset will be 45 minutes")


    df_runtime=df_movies[df_movies["runtime"] > 0]

    fig = px.box(
    df_runtime,
    y="runtime",
    title="Distribution of movies run time"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("📊 VISUALIZATION 5")

    st.write("INSIGHTS")
    st.write("Genre of Drama have highest no.of movies (937)")
    st.write("Genre of documentry have least no.of movies (1)")

    df_genre_count = (
    df_movie_genres
    .merge(df_genres, on="genre_id", how="left")
    .groupby("genre_name")["movie_id"]
    .nunique()
    .reset_index(name="movie_count")
    )

    fig = px.bar(
    df_genre_count,
    x="genre_name",
    y="movie_count",
    title="Count of Movies per Genre"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("📊 VISUALIZATION 6")
    
    st.write("INSIGHTS")
    st.write("High Budget movies secure high revenue (ex: avatar)")

    df_budget_revenue = df_movies[(df_movies["budget"] > 0) & (df_movies["revenue"] > 0)]

    fig = px.scatter(
    df_budget_revenue,
    x="budget",
    y="revenue",
    trendline="ols",
    hover_name="title",
    title="Movie vs Budget",
    labels = {"budget" : "Movie budget",
              "revenue" : "Movie revenue"}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("📊 VISUALIZATION 7")
        
    st.write("INSIGHTS")
    st.write("War genre movies got the highest avg rating")
    st.write("War genre movies got the highest avg rating")

    df_rating_genre = df_movie_genres.merge(
    df_genres,
    on="genre_id",
    how="left"
    )


    df_rating_genre = df_rating_genre.merge(
    df_movies[["movie_id", "vote_average"]],
    on="movie_id",
    how="left"
    )


    df_rating_genre = df_rating_genre.dropna(
    subset=["vote_average", "genre_name"]
    )


    df_avg_rating = (
    df_rating_genre
    .groupby("genre_name")["vote_average"]
    .mean()
    .reset_index(name="avg_rating")
    .sort_values("avg_rating")
    )


    fig = px.scatter(
    df_avg_rating,
    x="avg_rating",
    y="genre_name",
    title="Average Rating by Genre — Dot Plot",
    labels={
        "avg_rating": "Average Rating",
        "genre_name": "Genre"
    },
    text="avg_rating"
    )

    fig.update_traces(
    marker=dict(size=12),
    texttemplate="%{text:.2f}",
    textposition="middle right"
    )

    fig.update_layout(
    xaxis_range=[0, 10]
    )

    st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("📊 VISUALIZATION 8")
            
    st.write("INSIGHTS")
    st.write("Revenue and budget has strong correlation")
    st.write("Budget and vote_average has strong negative correlation")

    df_corr = df_movies[
    [
        "budget",
        "revenue",
        "runtime",
        "popularity",
        "vote_average",
        "vote_count"
    ]
    ]

    corr_matrix = df_corr.corr()

    fig = px.imshow(
    corr_matrix,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    title="Correlation Heatmap of Movie Features"
    )

    fig.update_layout(
    width=800,
    height=700
    )

    st.plotly_chart(fig, use_container_width=True)


else:
    selected == "Queries"

    st.title("Query Explorer")

    sql_tab, pandas_tab = st.tabs(
        ["SQL Analysis", "Pandas Analysis"]
    )



        
    
    with sql_tab:

        st.subheader("SQL Analysis")

    
        questions = [
            "List all movies in the Action genre released after 2015, showing title and release date.",
            "Find the top 10 highest-grossing movies along with the genre(s) each belongs to.",
            "Calculate the average budget and average revenue for each genre, sorted by average revenue descending",
            "List the top 10 actors who have appeared in the most movies in the dataset.(cast)",
            "Find all directors who have directed more than 3 movies, along with their movie count.",
            "List the top 10 most frequently used keywords across all movies.",
            "Find movies where the budget was above the overall average budget but the revenue was below the overall average revenue.",
            "List all actors who have appeared in a movie directed by a specific director (e.g., Christopher Nolan).",
            "Find the genre with the highest average rating, considering only genres with at least 20 movies.",
            "List the top 10 movies with the highest number of keywords tagged to them."
        ]

        selected_question = st.selectbox(
            "Select a sql Question",
            questions,
            key="sql_questions"
        )

        
        if selected_question == "List all movies in the Action genre released after 2015, showing title and release date.":
            query = """
            SELECT 
            m.title,
            m.release_date,
            m.day_name
            FROM movies AS m
            JOIN movie_genres AS mg ON m.movie_id = mg.movie_id
            JOIN genres AS g ON mg.genre_id = g.genre_id
            WHERE g.genre_name = 'Action' AND YEAR(m.release_date) > 2015;
            """

        elif selected_question == "Find the top 10 highest-grossing movies along with the genre(s) each belongs to.":
            query = """SELECT
            m.title,
            m.revenue,
            GROUP_CONCAT(DISTINCT g.genre_name ORDER BY g.genre_name SEPARATOR ', ') AS genres
            FROM movies AS m
            JOIN movie_genres AS mg ON m.movie_id = mg.movie_id
            JOIN genres AS g ON mg.genre_id = g.genre_id
            GROUP BY m.movie_id, m.title, m.revenue
            ORDER BY m.revenue DESC LIMIT 10;"""

        elif selected_question == "Calculate the average budget and average revenue for each genre, sorted by average revenue descending":
            query = """SELECT g.genre_name AS genre,
            AVG(m.budget) AS avg_budget,
            AVG(m.revenue) AS avg_revenue
            FROM movies AS m
            JOIN movie_genres AS mg ON m.movie_id = mg.movie_id
            JOIN genres AS g ON mg.genre_id = g.genre_id
            GROUP BY g.genre_id, g.genre_name
            ORDER BY avg_revenue DESC;"""

        elif selected_question == "List the top 10 actors who have appeared in the most movies in the dataset.(cast)":
            query = """SELECT c.actor_name AS actor_name,
            COUNT(DISTINCT c.movie_id) AS total_movies
            FROM casting AS c
            GROUP BY c.person_id, c.actor_name
            ORDER BY total_movies DESC LIMIT 10;"""

        elif selected_question == "Find all directors who have directed more than 3 movies, along with their movie count.":
            query = """SELECT person_id,
            person_name AS director_name,
            COUNT(DISTINCT movie_id) AS movie_count
            FROM crewing
            WHERE department = 'Directing' AND job = 'Director'
            GROUP BY person_id, person_name
            HAVING COUNT(DISTINCT movie_id) > 3
            ORDER BY movie_count DESC;"""

        elif selected_question == "List the top 10 most frequently used keywords across all movies.":
            query = """SELECT keyword_name AS keywords,
            COUNT(DISTINCT movie_id) AS movie_count
            FROM movie_keywords
            GROUP BY keyword_name
            ORDER BY movie_count DESC LIMIT 10;"""

        elif selected_question == "Find movies where the budget was above the overall average budget but the revenue was below the overall average revenue.":
            query = """SELECT title,budget,revenue
            FROM movies
            WHERE budget > (SELECT AVG(budget)FROM movies) AND revenue < (SELECT AVG(revenue)FROM movies);"""

        elif selected_question == "List all actors who have appeared in a movie directed by a specific director (e.g., Christopher Nolan).":
            query = """SELECT DISTINCT c.actor_name AS actor_name,c.person_id as person_id,M.title as title
            FROM casting AS c
            JOIN crewing AS cr ON c.movie_id = cr.movie_id
            JOIN movies AS M ON cr.movie_id = M.movie_id
            WHERE cr.person_name = 'James Cameron' AND cr.job = 'Director' AND cr.department = 'Directing'
            ORDER BY actor_name;"""

        elif selected_question == "Find the genre with the highest average rating, considering only genres with at least 20 movies.":
            query = """SELECT g.genre_name AS genre_name,
            AVG(m.vote_average) AS avg_rating,
            COUNT(DISTINCT m.movie_id) AS total_movies
            FROM movies AS m
            JOIN movie_genres AS mg ON m.movie_id = mg.movie_id
            JOIN genres AS g ON mg.genre_id = g.genre_id
            GROUP BY g.genre_id, g.genre_name
            HAVING COUNT(DISTINCT m.movie_id) >= 20
            ORDER BY avg_rating DESC LIMIT 1;"""

        elif selected_question == "List the top 10 movies with the highest number of keywords tagged to them.":
            query = """SELECT
            m.title,
            COUNT(DISTINCT k.keyword_name) AS total_keywords
            FROM movies AS m
            JOIN movie_keywords AS k ON m.movie_id = k.movie_id
            GROUP BY m.movie_id, m.title
            ORDER BY total_keywords DESC LIMIT 10;"""

        # 3. Show query and execute it
        if query is not None:

            st.subheader("SQL Query")
            st.code(query, language="sql")

            if st.button("Run Query", key="run_sql_query"):

                try:
                    
                    result = pd.read_sql(query, con=engine)

                    st.subheader("Query Result")
                    st.dataframe(
                        result,
                        use_container_width=True
                    )

                    if selected_question == "List all movies in the Action genre released after 2015, showing title and release date.":

                        st.subheader("Text Insight")

                        if not result.empty and "release_date" in result.columns:
                            st.info(
                                f"This result shows {len(result)} Action movies "
                                "released after 2015."
                            )

                        else:
                            st.info("No movie data available for this insight.")

                        if "release_date" in result.columns:
                            result["release_date"] = pd.to_datetime(
                                result["release_date"], errors="coerce"
                            )
                            result["year"] = result["release_date"].dt.year

                            chart_data = (
                                result.groupby("year")
                                .size()
                                .reset_index(name="movie_count")
                            )

                            st.subheader("Chart")
                            st.bar_chart(chart_data, x="year", y="movie_count")


                    elif selected_question == "Find the top 10 highest-grossing movies along with the genre(s) each belongs to.":

                        st.subheader("Text Insight")

                        if not result.empty and "revenue" in result.columns:
                            top_movie = result.loc[result["revenue"].idxmax()]

                            st.info(
                                f"Highest-grossing movie in this result: "
                                f"{top_movie['title']}, with revenue "
                                f"{top_movie['revenue']:,.0f}."
                            )

                        if "title" in result.columns and "revenue" in result.columns:
                            st.subheader("Chart")

                            fig = px.bar(
                                result, x="revenue", y="title",
                                orientation="h", title="Movie Revenue"
                            )

                            st.plotly_chart(fig, use_container_width=True)


                    elif selected_question == "Calculate the average budget and average revenue for each genre, sorted by average revenue descending":

                        st.subheader("Text Insight")

                        if not result.empty and "avg_revenue" in result.columns:
                            top_genre = result.loc[result["avg_revenue"].idxmax()]

                            st.info(
                                f"{top_genre['genre']} has the highest "
                                f"average revenue in this result: "
                                f"{top_genre['avg_revenue']:,.0f}."
                            )

                        if (
                            "genre" in result.columns
                            and "avg_budget" in result.columns
                            and "avg_revenue" in result.columns
                        ):
                            st.subheader("Chart")

                            fig = px.bar(
                                result, x="genre",
                                y=["avg_budget", "avg_revenue"],
                                barmode="group",
                                title="Average Budget vs Revenue by Genre"
                            )

                            st.plotly_chart(fig, use_container_width=True)


                    elif selected_question == "List the top 10 actors who have appeared in the most movies in the dataset.(cast)":

                        st.subheader("Text Insight")

                        if not result.empty and "total_movies" in result.columns:
                            top_actor = result.loc[result["total_movies"].idxmax()]

                            st.info(
                                f"{top_actor['actor_name']} has the highest movie "
                                f"appearance count in this result: "
                                f"{top_actor['total_movies']}."
                            )

                        if "actor_name" in result.columns and "total_movies" in result.columns:
                            st.subheader("Chart")

                            fig = px.bar(
                                result, x="total_movies", y="actor_name",
                                orientation="h", title="Top Actors by Movie Count"
                            )

                            st.plotly_chart(fig, use_container_width=True)


                    elif selected_question == "Find all directors who have directed more than 3 movies, along with their movie count.":

                        st.subheader("Text Insight")

                        if not result.empty and "movie_count" in result.columns:
                            top_director = result.loc[result["movie_count"].idxmax()]

                            st.info(
                                f"{top_director['director_name']} directed the most movies "
                                f"in this result: {top_director['movie_count']}."
                            )

                        if "director_name" in result.columns and "movie_count" in result.columns:
                            st.subheader("Chart")

                            fig = px.bar(
                                result, x="movie_count", y="director_name",
                                orientation="h", title="Movies Directed by Each Director"
                            )

                            st.plotly_chart(fig, use_container_width=True)


                    elif selected_question == "List the top 10 most frequently used keywords across all movies.":

                        st.subheader("Text Insight")

                        if not result.empty and "movie_count" in result.columns:
                            top_keyword = result.loc[result["movie_count"].idxmax()]

                            st.info(
                                f"The most frequently used keyword in this result is "
                                f"{top_keyword['keywords']}, appearing "
                                f"{top_keyword['movie_count']} times."
                            )

                        if "keywords" in result.columns and "movie_count" in result.columns:
                            st.subheader("Chart")

                            fig = px.bar(
                                result, x="movie_count", y="keywords",
                                orientation="h", title="Most Frequently Used Keywords"
                            )

                            st.plotly_chart(fig, use_container_width=True)


                    elif selected_question == "Find movies where the budget was above the overall average budget but the revenue was below the overall average revenue.":

                        st.subheader("Text Insight")

                        if not result.empty and "budget" in result.columns and "revenue" in result.columns:
                            st.info(
                                f"This query returned {len(result)} movies with "
                                "above-average budget and below-average revenue."
                            )

                        if "budget" in result.columns and "revenue" in result.columns:
                            st.subheader("Chart")

                            fig = px.scatter(
                                result, x="budget", y="revenue",
                                hover_name="title" if "title" in result.columns else None,
                                title="Budget vs Revenue"
                            )

                            st.plotly_chart(fig, use_container_width=True)


                    elif selected_question == "List all actors who have appeared in a movie directed by a specific director (e.g., Christopher Nolan).":

                        st.subheader("Text Insight")

                        if not result.empty and "actor_name" in result.columns:
                            st.info(
                                f"The result lists {result['actor_name'].nunique()} "
                                "unique actors across the selected director's movies."
                            )

                        if "title" in result.columns and "actor_name" in result.columns:
                            chart_data = (
                                result.groupby("title")["actor_name"]
                                .nunique()
                                .reset_index(name="actor_name")
                            )

                            st.subheader("Chart")

                            fig = px.bar(
                                chart_data, x="title", y="actor_name",
                                title="Number of Actors per Movie"
                            )

                            st.plotly_chart(fig, use_container_width=True)


                    elif selected_question == "Find the genre with the highest average rating, considering only genres with at least 20 movies.":

                        st.subheader("Text Insight")

                        if not result.empty and "avg_rating" in result.columns:
                            top_genre = result.loc[result["avg_rating"].idxmax()]

                            st.info(
                                f"{top_genre['genre_name']} has the highest average "
                                f"rating in this result: {top_genre['avg_rating']:.2f}."
                            )

                        if "genre_name" in result.columns and "avg_rating" in result.columns:
                            st.subheader("Chart")

                            fig = px.bar(
                                result, x="genre_name", y="avg_rating",
                                title="Average Rating by Genre"
                            )

                            st.plotly_chart(fig, use_container_width=True)


                    elif selected_question == "List the top 10 movies with the highest number of keywords tagged to them.":

                        st.subheader("Text Insight")

                        if not result.empty and "total_keywords" in result.columns:
                            top_movie = result.loc[result["total_keywords"].idxmax()]

                            st.info(
                                f"{top_movie['title']} has the highest keyword count "
                                f"in this result: {top_movie['total_keywords']}."
                            )

                        if "title" in result.columns and "total_keywords" in result.columns:
                            st.subheader("Chart")

                            fig = px.bar(
                                result, x="total_keywords", y="title",
                                orientation="h", title="Movies by Keyword Count"
                            )

                            st.plotly_chart(fig, use_container_width=True)

                

                        else:
                            st.info("Title or keyword count column not found.")

                    
                    
                    

                except Exception as e:
                    st.exception(e)

        else:
            st.info(
                "Sql query not added for this question"
            )


    
    
    with pandas_tab:

        st.subheader("Pandas Analysis")

        questions = {
            "1. Unique movies, genres, cast and crew members":
                "1",
            "2. Movies with missing or zero budget/revenue":
                "2",
            "3. Profit and ROI for valid movies":
                "3",
            "4. Top 15 movies by ROI (budget >= $1 million)":
                "4",
            "5. Movies released per year":
                "5",
            "6. Runtime outliers":
                "6",
            "7. Primary genre and average popularity":
                "7",
            "8. Top 10 actors and average movie rating":
                "8",
            "9. Duplicate movie titles and release years":
                "9",
            "10. Unusual popularity and vote count":
                "10"
        }

        selected_question = st.selectbox(
            "Select a Pandas Question",
            list(questions.keys()),
            key="pandas_question"
        )

        question_number = questions[selected_question]

        pandas_code = {

            "1": '''print(
        "Unique Movies:", df_movies["movie_id"].nunique(),
        "\\nUnique Genres:", df_genres["genre_id"].nunique(),
        "\\nUnique Cast Members:", df_cast["person_id"].nunique(),
        "\\nUnique Crew Members:", df_crew["person_id"].nunique()
    )''',

            "2": '''result = df_movies[
        df_movies["budget"].isna()
        | df_movies["revenue"].isna()
        | (df_movies["budget"] == 0)
        | (df_movies["revenue"] == 0)
    ][["movie_id", "title", "budget", "revenue"]]''',

            "3": '''valid_movies = df_movies[
        df_movies["budget"].notna()
        & df_movies["revenue"].notna()
        & (df_movies["budget"] > 0)
    ].copy()

    valid_movies["profit"] = (
        valid_movies["revenue"] - valid_movies["budget"]
    )

    valid_movies["ROI"] = (
        valid_movies["profit"] / valid_movies["budget"]
    ) * 100

    result = valid_movies[
        ["title", "budget", "revenue", "profit", "ROI"]
    ]''',

            "4": '''valid_movies = df_movies[
        df_movies["budget"] >= 1000000
    ].copy()

    valid_movies["ROI"] = (
        (valid_movies["revenue"] - valid_movies["budget"])
        / valid_movies["budget"]
    ) * 100

    result = valid_movies.dropna(
        subset=["ROI"]
    ).sort_values(
        "ROI", ascending=False
    )[["title", "budget", "profit", "ROI"]].head(15)''',

            "5": '''result = (
        df_movies["year"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    result.columns = ["year", "movie_count"]''',

            "6": '''Q1 = df_movies["runtime"].quantile(0.25)
    Q3 = df_movies["runtime"].quantile(0.75)

    IQR = Q3 - Q1

    result = df_movies[
        (df_movies["runtime"] < Q1 - 1.5 * IQR)
        | (df_movies["runtime"] > Q3 + 1.5 * IQR)
    ][["movie_id", "title", "runtime"]]''',

            "7": '''primary_genres = (
        df_movie_genres
        .sort_values("genre_id")
        .drop_duplicates(subset="movie_id", keep="first")
        .merge(df_genres, on="genre_id", how="left")
        .merge(
            df_movies[["movie_id", "title", "popularity"]],
            on="movie_id", how="left"
        )
    )

    result = primary_genres[
        ["movie_id", "title", "genre_name", "popularity"]
    ]''',

            "8": '''top_10_actors = (
        df_cast
        .merge(
            df_movies[["movie_id", "vote_average"]],
            on="movie_id", how="left"
        )
        .groupby(["person_id", "actor_name"])
        .agg(
            movie_count=("movie_id", "nunique"),
            avg_rating=("vote_average", "mean")
        )
        .sort_values("movie_count", ascending=False)
        .head(10)
        .reset_index()
    )

    result = top_10_actors''',

            "9": '''result = (
        df_movies[
            df_movies.duplicated(subset="title", keep=False)
        ]
        .sort_values("title")
        [["title", "year"]]
    )''',

            "10": '''pop_high = df_movies["popularity"].quantile(0.75)
    pop_low = df_movies["popularity"].quantile(0.25)

    vote_high = df_movies["vote_count"].quantile(0.75)
    vote_low = df_movies["vote_count"].quantile(0.25)

    result = df_movies[
        (
            (df_movies["popularity"] >= pop_high)
            & (df_movies["vote_count"] <= vote_low)
        )
        | (
            (df_movies["popularity"] <= pop_low)
            & (df_movies["vote_count"] >= vote_high)
        )
    ][["title", "popularity", "vote_count"]].sort_values(
        "popularity", ascending=False
    )'''
        }

        st.subheader("Pandas Code")
        st.code(pandas_code[question_number], language="python")

        if st.button("Run Query", key="run_pandas_query"):

            try:

                result = pd.DataFrame()
                chart_data = pd.DataFrame()

                # Question 1
                if question_number == "1":

                    result = pd.DataFrame({
                        "Category": [
                            "Movies", "Genres",
                            "Cast Members", "Crew Members"
                        ],
                        "Count": [
                            df_movies["movie_id"].nunique(),
                            df_genres["genre_id"].nunique(),
                            df_cast["person_id"].nunique(),
                            df_crew["person_id"].nunique()
                        ]
                    })

                    st.subheader("Text Insight")

                    highest = result.loc[result["Count"].idxmax()]

                    st.info(
                        f"{highest['Category']} has the highest "
                        f"unique count: {highest['Count']:,}."
                    )

                    chart_data = result

                    st.subheader("Chart")

                    fig = px.bar(
                        chart_data,
                        x="Category",
                        y="Count",
                        title="Unique Records Across Tables"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 2
                elif question_number == "2":

                    result = df_movies[
                        df_movies["budget"].isna()
                        | df_movies["revenue"].isna()
                        | (df_movies["budget"] == 0)
                        | (df_movies["revenue"] == 0)
                    ][["movie_id", "title", "budget", "revenue"]]

                    st.subheader("Text Insight")

                    st.info(
                        f"{len(result):,} movies have missing or zero "
                        "budget or revenue. Treat zero financial values "
                        "as unknown when the dataset does not confirm "
                        "that zero is genuine."
                    )

                    chart_data = pd.DataFrame({
                        "Value Type": ["Missing Budget", "Zero Budget",
                                    "Missing Revenue", "Zero Revenue"],
                        "Movie Count": [
                            df_movies["budget"].isna().sum(),
                            (df_movies["budget"] == 0).sum(),
                            df_movies["revenue"].isna().sum(),
                            (df_movies["revenue"] == 0).sum()
                        ]
                    })

                    st.subheader("Chart")

                    fig = px.bar(
                        chart_data,
                        x="Value Type",
                        y="Movie Count",
                        title="Missing and Zero Financial Values"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 3
                elif question_number == "3":

                    valid_movies = df_movies[
                        df_movies["budget"].notna()
                        & df_movies["revenue"].notna()
                        & (df_movies["budget"] > 0)
                    ].copy()

                    valid_movies["profit"] = (
                        valid_movies["revenue"] - valid_movies["budget"]
                    )

                    valid_movies["ROI"] = (
                        valid_movies["profit"] / valid_movies["budget"]
                    ) * 100

                    result = valid_movies[
                        ["title", "budget", "revenue", "profit", "ROI"]
                    ]

                    st.subheader("Text Insight")

                    if not result.empty:
                        best = result.loc[result["ROI"].idxmax()]

                        st.info(
                            f"{best['title']} has the highest ROI "
                            f"in this result: {best['ROI']:.2f}%."
                        )

                    st.subheader("Chart")

                    fig = px.scatter(
                        result,
                        x="budget",
                        y="revenue",
                        hover_name="title",
                        title="Movie Budget vs Revenue"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 4
                elif question_number == "4":

                    valid_movies = df_movies[
                        (df_movies["budget"] >= 1000000)
                        & df_movies["revenue"].notna()
                    ].copy()

                    valid_movies["profit"] = (
                        valid_movies["revenue"] - valid_movies["budget"]
                    )

                    valid_movies["ROI"] = (
                        valid_movies["profit"] / valid_movies["budget"]
                    ) * 100

                    result = valid_movies.sort_values(
                        "ROI", ascending=False
                    )[["title", "budget", "profit", "ROI"]].head(15)

                    st.subheader("Text Insight")

                    if not result.empty:
                        best = result.iloc[0]

                        st.info(
                            f"{best['title']} ranks first by ROI among "
                            f"movies with a budget of at least $1 million: "
                            f"{best['ROI']:.2f}%."
                        )

                    st.subheader("Chart")

                    fig = px.bar(
                        result,
                        x="ROI",
                        y="title",
                        orientation="h",
                        title="Top 15 Movies by ROI"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 5
                elif question_number == "5":

                    result = (
                        df_movies["year"]
                        .value_counts()
                        .sort_index()
                        .reset_index()
                    )

                    result.columns = ["year", "movie_count"]
                    result = result.dropna(subset=["year"])

                    st.subheader("Text Insight")

                    if not result.empty:
                        peak = result.loc[result["movie_count"].idxmax()]

                        st.info(
                            f"The year {int(peak['year'])} has the highest "
                            f"movie output: {int(peak['movie_count']):,} movies."
                        )

                    st.subheader("Chart")

                    fig = px.line(
                        result,
                        x="year",
                        y="movie_count",
                        markers=True,
                        title="Movies Released per Year"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 6
                elif question_number == "6":

                    Q1 = df_movies["runtime"].quantile(0.25)
                    Q3 = df_movies["runtime"].quantile(0.75)
                    IQR = Q3 - Q1

                    result = df_movies[
                        (df_movies["runtime"] < Q1 - 1.5 * IQR)
                        | (df_movies["runtime"] > Q3 + 1.5 * IQR)
                    ][["movie_id", "title", "runtime"]]

                    st.subheader("Text Insight")

                    st.info(
                        f"Found {len(result):,} runtime outliers using "
                        "the IQR method. These are unusually short or "
                        "long compared with the dataset."
                    )

                    st.subheader("Chart")

                    fig = px.scatter(
                        result,
                        x="title",
                        y="runtime",
                        hover_name="title",
                        title="Runtime Outlier Movies"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 7
                elif question_number == "7":

                    primary_genres = (
                        df_movie_genres
                        .sort_values("genre_id")
                        .drop_duplicates(subset="movie_id", keep="first")
                        .merge(df_genres, on="genre_id", how="left")
                        .merge(
                            df_movies[["movie_id", "title", "popularity"]],
                            on="movie_id", how="left"
                        )
                    )

                    result = primary_genres[
                        ["movie_id", "title", "genre_name", "popularity"]
                    ]

                    chart_data = (
                        result.groupby("genre_name")["popularity"]
                        .mean()
                        .sort_values(ascending=False)
                        .reset_index()
                    )

                    st.subheader("Text Insight")

                    if not chart_data.empty:
                        best = chart_data.iloc[0]

                        st.info(
                            f"{best['genre_name']} has the highest "
                            f"average popularity as a primary genre: "
                            f"{best['popularity']:.2f}."
                        )

                    st.subheader("Chart")

                    fig = px.bar(
                        chart_data,
                        x="genre_name",
                        y="popularity",
                        title="Average Popularity by Primary Genre"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 8
                elif question_number == "8":

                    result = (
                        df_cast
                        .merge(
                            df_movies[["movie_id", "vote_average"]],
                            on="movie_id", how="left"
                        )
                        .groupby(["person_id", "actor_name"])
                        .agg(
                            movie_count=("movie_id", "nunique"),
                            avg_rating=("vote_average", "mean")
                        )
                        .sort_values("movie_count", ascending=False)
                        .head(10)
                        .reset_index()
                    )

                    st.subheader("Text Insight")

                    if not result.empty:
                        top_actor = result.iloc[0]

                        st.info(
                            f"{top_actor['actor_name']} appears in the most "
                            f"movies in this result ({top_actor['movie_count']}) "
                            f"with an average movie rating of "
                            f"{top_actor['avg_rating']:.2f}."
                        )

                    st.subheader("Chart")

                    fig = px.bar(
                        result,
                        x="movie_count",
                        y="actor_name",
                        orientation="h",
                        hover_data=["avg_rating"],
                        title="Top 10 Actors by Movie Count"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 9
                elif question_number == "9":

                    result = (
                        df_movies[
                            df_movies.duplicated(subset="title", keep=False)
                        ]
                        .sort_values("title")
                        [["title", "year"]]
                    )

                    st.subheader("Text Insight")

                    duplicate_count = result["title"].nunique()

                    st.info(
                        f"Found {duplicate_count:,} movie titles that "
                        "appear more than once. Repeated titles may be "
                        "remakes or duplicate records; check release years."
                    )

                    chart_data = (
                        result.groupby("title")
                        .size()
                        .reset_index(name="record_count")
                        .sort_values("record_count", ascending=False)
                        .head(15)
                    )

                    st.subheader("Chart")

                    fig = px.bar(
                        chart_data,
                        x="title",
                        y="record_count",
                        title="Repeated Movie Titles (Top 15)"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Question 10
                elif question_number == "10":

                    pop_high = df_movies["popularity"].quantile(0.75)
                    pop_low = df_movies["popularity"].quantile(0.25)

                    vote_high = df_movies["vote_count"].quantile(0.75)
                    vote_low = df_movies["vote_count"].quantile(0.25)

                    result = df_movies[
                        (
                            (df_movies["popularity"] >= pop_high)
                            & (df_movies["vote_count"] <= vote_low)
                        )
                        | (
                            (df_movies["popularity"] <= pop_low)
                            & (df_movies["vote_count"] >= vote_high)
                        )
                    ][["title", "popularity", "vote_count"]].sort_values(
                        "popularity", ascending=False
                    )

                    st.subheader("Text Insight")

                    st.info(
                        f"Found {len(result):,} movies with unusual combinations "
                        "of popularity and vote count based on the 25th and "
                        "75th percentiles."
                    )

                    st.subheader("Chart")

                    fig = px.scatter(
                        result,
                        x="vote_count",
                        y="popularity",
                        hover_name="title",
                        title="Unusual Popularity vs Vote Count"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                # Display the selected question's result
                st.subheader("Pandas Result")
                st.dataframe(result, use_container_width=True)

            except Exception as e:
                st.error(f"Pandas analysis failed: {e}")
                st.exception(e)



            
        







