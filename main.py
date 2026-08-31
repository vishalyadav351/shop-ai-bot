from fastapi import FastAPI, Request, Response, Form
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

# Tumhari dukan ka product menu aur prices
PRODUCTS = {
    "laptop": {"price": "45,000 INR", "desc": "High performance laptop with 16GB RAM."},
    "mouse": {"price": "500 INR", "desc": "Wireless optical mouse."},
    "keyboard": {"price": "800 INR", "desc": "RGB mechanical gaming keyboard."},
    "headphones": {"price": "1,500 INR", "desc": "Bluetooth over-ear headphones with deep bass."}
}

@app.get("/")
async def root():
    return {"status": "success", "message": "WhatsApp Shop Bot is Live on Cloud!"}

@app.post("/webhook")
async def receive_message(Body: str = Form(...), From: str = Form(...)):
    try:
        # Customer ka message lowercase me convert karenge taaki match karna aasan ho
        msg = Body.strip().lower()
        print(f"\n--- New Message ---")
        print(f"From: {From}")
        print(f"Message: {msg}")
        
        resp = MessagingResponse()
        reply_msg = resp.message()

        # Agar customer "hi", "hello" ya "menu" bole
        if msg in ["hi", "hello", "menu", "start"]:
            reply_msg.body(
                "🙏 Namaste! Hamari dukan mein aapka swagat hai.\n\n"
                "Aap kya kharidna chahte hain? In items ke naam bhejiye:\n"
                "• *Laptop*\n"
                "• *Mouse*\n"
                "• *Keyboard*\n"
                "• *Headphones*\n\n"
                "Ya fir kisi bhi item ka naam type karein info ke liye!"
            )
        
        # Agar customer ne dukan ke product ka naam pucha ho
        elif msg in PRODUCTS:
            item = PRODUCTS[msg]
            reply_msg.body(
                f"📦 *{msg.capitalize()}* ki details:\n"
                f"💰 Price: {item['price']}\n"
                f"📝 Details: {item['desc']}\n\n"
                f"Kya aap ise order karna chahte hain? 'Yes' ya 'No' likhein."
            )
        
        # Agar item dukan me na ho ya galat naam likha ho
        else:
            reply_msg.body(
                f"🙏 Maaf kijiye, '{Body}' hamari dukan mein abhi available nahi hai.\n"
                "Menu dekhne ke liye **'Menu'** type karke bhejiye."
            )

        return Response(content=str(resp), media_type="application/xml")
        
    except Exception as e:
        print(f"Error aaya: {str(e)}")
        return {"status": "error", "message": str(e)}