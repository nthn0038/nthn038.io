from js import document
from math import sin, cos, pi
import asyncio

async def draw_heart(ctx, x, y, w, h, color):
    ctx.beginPath()
    ctx.moveTo(x, y)
    ctx.fillStyle = color
    a = 0
    while a < 2 * pi:
        xOffset = w * (16 * (sin(a) ** 3))
        yOffset = h * (13 * cos(a) - 5 * cos(2 * a) - 2 * cos(3 * a) - cos(4 * a))
        ctx.lineTo(x + xOffset, y - yOffset)
        a += 0.02
        await asyncio.sleep(0.01)  
        ctx.stroke()
    ctx.closePath()
    ctx.fill()

async def draw_text(ctx, x, y, text):
    ctx.fillStyle = 'white'
    ctx.font = '15px verdana bold'
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    ctx.fillText(text, x, y)

async def main():
    canvas = document.getElementById('heartCanvas')
    ctx = canvas.getContext('2d')
    colors = ['#d90166', 'purple', 'blue']
    w = 16
    h = 16
    for color in colors:
        await draw_heart(ctx, canvas.width / 2, canvas.height / 2, w, h, color)
        w -= 3
        h -= 2
    
    await draw_text(ctx, canvas.width / 2, canvas.height / 2, "sana makapag phasmo bossing 🙏🙏🙏🙏🙏🙏")

asyncio.ensure_future(main())
