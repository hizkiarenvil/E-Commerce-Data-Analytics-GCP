import pandas as pd
from typing import Optional, List

def load_ecommerce_data(file_path: str = 'e_commerce_data.csv') -> Optional[pd.DataFrame]:
    """
    Load e-commerce data from CSV file with error handling
    
    Args:
        file_path: Path to CSV file
        
    Returns:
        DataFrame if successful, None otherwise
    """
    try:
        df = pd.read_csv(file_path, encoding='latin1')
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert column names to lowercase with underscores"""
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values in specific columns"""
    print("\nHandling missing values:")
    
    # Description column
    if 'description' in df.columns:
        missing_desc = df['description'].isna().sum()
        df['description'].fillna('Unknown', inplace=True)
        print(f"- Imputed {missing_desc} missing descriptions with 'Unknown'")
    
    # Numeric columns
    numeric_cols = ['quantity', 'unitprice']
    for col in numeric_cols:
        if col in df.columns:
            missing_vals = df[col].isna().sum()
            # Handle negative values
            negative_count = (df[col] < 0).sum()
            if negative_count > 0:
                df[col] = df[col].clip(lower=0)
                print(f"- Corrected {negative_count} negative values in {col}")
            # Impute missing values
            if missing_vals > 0:
                col_mean = df[col].mean()
                df[col].fillna(col_mean, inplace=True)
                print(f"- Imputed {missing_vals} missing values in {col} with mean {col_mean:.2f}")
    
    return df

def remove_duplicates(df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Remove duplicate rows with configurable subset
    
    Args:
        df: Input DataFrame
        subset: Columns to consider for duplicates detection
    
    Returns:
        Cleaned DataFrame
    """
    if subset is None:
        subset = df.columns.difference(['customerid'])
    
    initial_rows = len(df)
    duplicates = df.duplicated(subset=subset, keep='first')
    
    print(f"\nDuplicate handling:")
    print(f"- Found {duplicates.sum()} duplicate rows")
    
    df = df[~duplicates].reset_index(drop=True)
    print(f"- Removed {initial_rows - len(df)} duplicates")
    
    return df

def convert_datetime(df: pd.DataFrame, col: str = 'invoicedate') -> pd.DataFrame:
    """Convert specified column to datetime format"""
    if col in df.columns:
        initial_nat = df[col].isna().sum()
        df[col] = pd.to_datetime(df[col], format='%m/%d/%Y %H:%M', errors='coerce')
        new_nat = df[col].isna().sum() - initial_nat
        
        if new_nat > 0:
            print(f"\nDate conversion:")
            print(f"- Found {new_nat} invalid datetime values converted to NaT")
    
    return df

def main():
    # Load and initial processing
    df = load_ecommerce_data()
    if df is None:
        return
    
    # Cleaning pipeline
    df = (
        df
        .pipe(clean_column_names)
        .pipe(handle_missing_values)
        .pipe(remove_duplicates)
        .pipe(convert_datetime)
    )
    
    # Final report
    print("\nCleaning process completed successfully.")
    print("\nFinal DataFrame Summary:")
    print(df.info())
    print("\nSample data:")
    print(df.head(3))

if __name__ == "__main__":
    main()
