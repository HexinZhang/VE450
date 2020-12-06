#!/usr/bin/env python
# coding: utf-8

# In[ ]:



from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Liquid, Page, Pie, Gauge,Timeline
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
import xlrd
import numpy as np
import pandas as pd
Grid=np.array(grid.value)
Battery=np.array(battery.value)
PV=np.array(data['Ppv'].values)
demand=np.array(data['Pcharge'].values)
demand=demand.tolist()
time=data['Time'].values
time=time.tolist()

batteryenergy=np.array(battery_sum)
for i in range(60):
    time[i+60]=time[i+60]+"pm"
saved_energy=[None]*121
saved_energy[0]=0

for i in range(120):
    saved_energy[i+1]=saved_energy[i]+PV[i]/5
saved_energy=saved_energy[1:121]

def print_line():
    x_data=range(0,len(Grid)) 
    timeline2= Timeline(init_opts=opts.InitOpts(bg_color="black"))
    for i in range(len(Grid)):
        line=(
            Line(init_opts=opts.InitOpts(bg_color="black"))
            .add_xaxis(xaxis_data=time[0:i+1])
            .add_yaxis(
                series_name="grid",
                y_axis=Grid[0:i+1],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=3,color="rgb(255,0,255)",),
                color="rgb(255,255,0)",
                symbol="diamond",
                symbol_size=2,
            )
            
            .add_yaxis(
                series_name="pv",
                y_axis=PV[0:i+1],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=3,color="rgb(0,255,255)"),
               color="rgb(255,255,255)",
             symbol="circle",
                symbol_size=2,
            )
             .add_yaxis(
                series_name="battery",
                y_axis=Battery[0:i+1],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=3,color="rgb(255,255,255)"),
               color="rgb(0,255,255)",
             symbol="triangle",
                symbol_size=2,
            )
             .add_yaxis(
                series_name="demand",
                y_axis=demand[0:i+1],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=3,color="rgb(255,255,0)"),
               color="rgb(255,0,255)",
             symbol="rect",
                symbol_size=2,
            )
  
            .set_global_opts(
                title_opts=opts.TitleOpts(title="PV, battery, demand, grid(kW) till time {}".format (time[i]),title_textstyle_opts=opts.TextStyleOpts(color="white")),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="none"),
                xaxis_opts=opts.AxisOpts(
                boundary_gap=False,
                min_='dataMin',
                max_='dataMax',
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="white"),),
                axislabel_opts=opts.LabelOpts(),),
                yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}"),
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="white")),
                splitline_opts=opts.SplitLineOpts(is_show=True),),
                visualmap_opts=opts.VisualMapOpts(
                    is_show=False,
                    is_piecewise=False,
                    dimension=0,
                    textstyle_opts=opts.TextStyleOpts(color="white")

                ),
                legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white"),pos_left="right",pos_top="5%"),
            ))
        timeline2.add(line, "{}年".format(i)).add_schema(play_interval=2000,is_auto_play=True,is_timeline_show=False)
    timeline2.render("C:/Users/suqi/Desktop/allcode/linenew.html")
print_line()
def print_gauge():
    timeline3= Timeline(init_opts=opts.InitOpts(bg_color="black"))
    for i in range(len(Grid)):
        b=batteryenergy[i]/900*100
        
        gauge0=(
          Gauge(init_opts=opts.InitOpts(bg_color="black"))
          .add(series_name="grid", data_pair=[["",round(b,1)]],max_=100,min_=0,
                start_angle=210,
                split_number=5,
                end_angle = -30,
           axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=20)),
           detail_label_opts=opts.LabelOpts(formatter="{value}%",),
            radius="80%" )
          .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
            title_opts=opts.TitleOpts("Percentage of battery energy at time {}".format (time[i]),title_textstyle_opts=opts.TextStyleOpts(color="white"))
        )
        )
        timeline3.add(gauge0, "{}年".format(i)).add_schema(is_timeline_show=True).add_schema(play_interval=2000,is_auto_play=True,is_timeline_show=False)
    timeline3.render("C:/Users/suqi/Desktop/allcode/gaugenew.html")
print_gauge()
def print_bar():
    x = ["no PV","PV"]
    timeline1= Timeline(init_opts=opts.InitOpts(bg_color="black"))
    for i in range(len(Grid)):
        price_noPV[i]=('%.2f' %  price_noPV[i])
        price_opti[i]=('%.2f' %  price_opti[i])
        bar = (
            Bar(init_opts=opts.InitOpts(bg_color="black"))
            .add_xaxis(x)
            .add_yaxis("overall income",[price_noPV[i],price_opti[i]], color="rgb(30,144,255)",label_opts=opts.LabelOpts() )
           
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="The overall income(USD) till time {}".format(time[i]),title_textstyle_opts=opts.TextStyleOpts(color="white")),
                              yaxis_opts=opts.AxisOpts(
                                                       axisline_opts=opts.AxisLineOpts(
                                                       linestyle_opts=opts.LineStyleOpts(color="white"),
            ),
                                                        axislabel_opts=opts.LabelOpts() ),

                             xaxis_opts=opts.AxisOpts(
                                                       axisline_opts=opts.AxisLineOpts(
                                                       linestyle_opts=opts.LineStyleOpts(color="white")
            ),
                                axislabel_opts=opts.LabelOpts() ),
                             legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white"),pos_left="right",pos_top="0%"),)

           )
       
        timeline1.add(bar,"{}年".format(i)).add_schema(play_interval=2000,is_auto_play=True,is_timeline_show=False)   
    timeline1.render("C:/Users/suqi/Desktop/allcode/barnew.html")
print_bar()

    

def bar1() -> Timeline:
    x = ["No PV","PV"]
    timeline1= Timeline(init_opts=opts.InitOpts(width="270px", height="180px",bg_color="black"))
    for i in range(len(Grid)):
       ## print(x)
        bar = (
            Bar(init_opts=opts.InitOpts(width="270px", height="180px",bg_color="black"))
            .add_xaxis(x)
           .add_yaxis("overall income",[price_noPV[i],price_opti[i]], color="rgb(30,144,255)",label_opts=opts.LabelOpts(font_size=10) )
           .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right",font_size=8))
            .set_global_opts(title_opts=opts.TitleOpts(title="The overall income(USD) till time {}".format(time[i]),title_textstyle_opts=opts.TextStyleOpts(color="white",font_size=10.5)),
                              yaxis_opts=opts.AxisOpts(
                                                       axisline_opts=opts.AxisLineOpts(
                                                       linestyle_opts=opts.LineStyleOpts(color="white"),
            ),
                                                        axislabel_opts=opts.LabelOpts(font_size=6) ),

                             xaxis_opts=opts.AxisOpts(
                                                       axisline_opts=opts.AxisLineOpts(
                                                       linestyle_opts=opts.LineStyleOpts(color="white"),
                                                           
            ),
                                axislabel_opts=opts.LabelOpts(font_size=8) ),
                             legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white",font_size=10),pos_left="right",pos_top="10%"),)

           )
        timeline1.add(bar,"{}年".format(i)).add_schema(play_interval=2000,is_auto_play=True,is_timeline_show=False)   
    return timeline1
def gauge1() -> Timeline:
    timeline3= Timeline(init_opts=opts.InitOpts(width="270px", height="180px",bg_color="black"))
    for i in range(len(Grid)):
        b=batteryenergy[i]/900*100
        
        gauge0=(
          Gauge(init_opts=opts.InitOpts(width="270px", height="180px", bg_color="black"))
          .add(series_name="grid", data_pair=[["",round(b,1)]],max_=100,min_=0,
                start_angle=210,
                split_number=5,
                end_angle = -30,
           axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=20)),
           detail_label_opts=opts.LabelOpts(formatter="{value}%",font_size=12),
            radius="80%" )
          .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{a} <br/>{b} : {c}%"),
            title_opts=opts.TitleOpts("Percentage of battery energy at time {}".format (time[i]),title_textstyle_opts=opts.TextStyleOpts(color="white",font_size=10.5))
        )
        )
        timeline3.add(gauge0, "{}年".format(i)).add_schema(is_timeline_show=True).add_schema(play_interval=2000,is_auto_play=True,is_timeline_show=False)
    return timeline3
def line2() -> Timeline:
    x_data=range(0,len(Grid))   
    timeline2= Timeline(init_opts=opts.InitOpts(width="270px", height="180px",bg_color="black"))
    for i in range(len(Grid)):
        line=(
            Line(init_opts=opts.InitOpts(width="270px", height="180px", bg_color="black"))
            .add_xaxis(xaxis_data=time[0:i+1])
            .add_yaxis(
                series_name="grid",
                y_axis=Grid[0:i+1],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=3,color="rgb(255,0,255)",),
                color="rgb(255,255,0)",
                symbol="diamond",
                symbol_size=2,
            )
            
            .add_yaxis(
                series_name="pv",
                y_axis=PV[0:i+1],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=3,color="rgb(0,255,255)"),
               color="rgb(255,255,255)",
             symbol="circle",
                symbol_size=2,
            )
             .add_yaxis(
                series_name="battery",
                y_axis=Battery[0:i+1],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=3,color="rgb(255,255,255)"),
               color="rgb(0,255,255)",
             symbol="triangle",
                symbol_size=2,
            )
             .add_yaxis(
                series_name="demand",
                y_axis=demand[0:i+1],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts=opts.LineStyleOpts(width=3,color="rgb(255,255,0)"),
               color="rgb(255,0,255)",
             symbol="rect",
                symbol_size=2,
            )
  
            .set_global_opts(
                title_opts=opts.TitleOpts(title="PV, battery, demand, grid(kW) till time {}".format (time[i]),title_textstyle_opts=opts.TextStyleOpts(color="white",font_size=10.5)),
                tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="none"),
                xaxis_opts=opts.AxisOpts(
                boundary_gap=False,
                min_='dataMin',
                max_='dataMax',
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="white"),),
                axislabel_opts=opts.LabelOpts(font_size=8),),
                yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}",font_size=8),
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="white")),
                splitline_opts=opts.SplitLineOpts(is_show=True),),
                visualmap_opts=opts.VisualMapOpts(
                    is_show=False,
                    is_piecewise=False,
                    dimension=0,
                    textstyle_opts=opts.TextStyleOpts(color="white")

                ),
                legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(color="white",font_size=9),pos_left="left",pos_top="10%",item_gap=5),
            ))
        timeline2.add(line, "{}年".format(i)).add_schema(play_interval=2000,is_auto_play=True,is_timeline_show=False)

    return timeline2






def page_simple_layout():
    page = Page()
    page.add(
       line2(),
         bar1(),
         gauge1(),
         
      
      
      
    )
    page.render("C:/Users/suqi/Desktop/allcode/page_simple_layoutnew.html")

if __name__ == "__main__":
    page_simple_layout()

