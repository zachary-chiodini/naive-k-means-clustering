import numpy as np, six
from matplotlib import rcParams
import matplotlib.pyplot as plt

def render_table( data, col_width = 3.0, row_height = 0.625, font_size = 14, title = '',
                  font = 'cambria', header_color = '#40466e', row_colors = ['#f1f1f2', 'w'],
                  edge_color = 'w', bbox = [0, 0, 1, 1], header_columns = 0, ax = None, **kwargs ) :
    
    rcParams[ 'font.family' ] = font
    rcParams.update( { 'font.size': font_size } )
    
    if ax is None :
        size = ( np.array( data.shape[::-1] ) + np.array( [ 0, 1 ] ) ) *\
                 np.array( [ col_width, row_height ] )
        fig, ax = plt.subplots( figsize = size )
        ax.axis( 'off' )

    table = ax.table(
        cellText = data.values,
        bbox = bbox,
        colLabels = data.columns,
        **kwargs
        )
    for k, cell in six.iteritems( table._cells ) :
        cell.set_edgecolor( edge_color )
        if k[ 0 ] == 0 or k[ 1 ] < header_columns :
            cell.set_text_props( weight = 'bold', color = 'w' )
            cell.set_facecolor( header_color )
        else :
            cell.set_facecolor( row_colors[ k[ 0 ]%len( row_colors ) ] )
    ax.set_title( title )
    return ax