import os
import pandas as pd
import matplotlib.pyplot as plt


# Data Loading & Cleaning

def load_clean_session(year, race, session, cache_path='../data/raw/'):
    """Load and return a FastF1 session with cache enabled"""
    import fastf1
    fastf1.Cache.enable_cache(cache_path)
    s = fastf1.get_session(year, race, session)
    s.load()
    return s


def filter_accurate_laps(laps, max_laptime=120):
    """Filter to accurate, non-deleted laps within laptime threshold"""
    laps = laps[laps['IsAccurate'] == True]
    laps = laps[laps['Deleted'] == False]
    laps = laps[laps['LapTime'] < max_laptime]
    return laps.dropna(subset=['LapTime', 'Position'])


def convert_timedelta_cols(df, cols):
    """Convert timedelta columns to float seconds"""
    for col in cols:
        df[col] = pd.to_timedelta(df[col]).dt.total_seconds()
    return df


def lap_time_stats(laps_df, group_by):
    """Return median, mean, and std of lap times grouped by a column"""
    return laps_df.groupby(group_by)['LapTime'].agg(
        median='median',
        mean='mean',
        std='std'
    ).round(3)


# Driver & Team Mapping

def get_driver_team_map(laps_df):
    """Return a dict mapping driver code to team name"""
    return dict(
        laps_df[['Driver', 'Team']]
        .drop_duplicates()
        .values
    )


def get_driver_colors(laps_df):
    """Return a dict mapping each driver to their team color"""
    team_colors = get_team_colors()
    driver_team = get_driver_team_map(laps_df)
    return {
        driver: team_colors.get(team, '#FFFFFF')
        for driver, team in driver_team.items()
    }


# Color Palettes

def get_team_colors():
    """Return official 2023 F1 team colors"""
    return {
        'Red Bull Racing': '#3671C6',
        'Mercedes':        '#6CD3BF',
        'Ferrari':         '#E8002D',
        'McLaren':         '#FF8000',
        'Aston Martin':    '#358C75',
        'Alpine':          '#FF87BC',
        'Williams':        '#64C4FF',
        'AlphaTauri':      '#5E8FAA',
        'Alfa Romeo':      '#C92D4B',
        'Haas F1 Team':    '#B6BABD'
    }


def get_compound_colors():
    """Return official F1 tyre compound colors"""
    return {
        'SOFT':         '#FF3333',
        'MEDIUM':       '#FFF200',
        'HARD':         '#FFFFFF',
        'INTERMEDIATE': '#39B54A',
        'WET':          '#0067FF'
    }


def get_circuit_colors():
    """Return colors for each circuit in the 2023 multi-race analysis"""
    return {
        'Monza':       '#E8002D',
        'Silverstone': '#6CD3BF',
        'Spa':         '#3671C6',
        'Bahrain':     '#FF8000',
        'Singapore':   '#FF87BC',
        'Monaco':      '#FFF200',
    }


# Plotting

def setup_dark_plot(figsize=(14, 6)):
    """Create a pre-styled dark background figure and axis"""
    fig, ax = plt.subplots(figsize=figsize, facecolor='#1a1a2e')
    ax.set_facecolor('#1a1a2e')
    ax.tick_params(colors='white')
    ax.grid(True, color='white', alpha=0.08, linewidth=0.5)
    return fig, ax


def style_dark_labels(ax, title, xlabel, ylabel, fontsize=14):
    """Apply white labels and title to a dark plot"""
    ax.set_title(title, color='white', fontsize=fontsize)
    ax.set_xlabel(xlabel, color='white')
    ax.set_ylabel(ylabel, color='white')


def save_figure(filename, output_dir='/home/bkm/Downloads/Desktop/F1 EDA Project/f1-eda/outputs/figures/'):
    """Save current matplotlib figure to outputs/figures/"""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    plt.savefig(path, dpi=150, bbox_inches='tight')
    print(f"Saved: {filename}")