from fastapi import FastAPI, Request, Response, Form
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

# Vision Optical Database & Products
PRODUCTS = {
    "titan frame": {"price": "₹2,499", "desc": "Titan Computer Frame + Blue Cut Lens"},
    "fastrack frame": {"price": "₹2,799", "desc": "Fastrack Computer Frame + Blue Cut Lens"},
    "progressive": {"price": "₹3,500", "desc": "Progressive Glasses"}
}

@app.get("/")
async def root():
    return {"status": "success", "message": "Vision Optical AI Bot is Live on Cloud!"}

@app.post("/webhook")
async def receive_message(Body: str = Form(...), From: str = Form(...)):
    try:
        msg = Body.strip().lower()
        print(f"\n--- New Message ---")
        print(f"From: {From}")
        print(f"Message: {msg}")
        
        resp = MessagingResponse()
        reply_msg = resp.message()

        # 1. Greeting & Welcome Flow
        if msg in ["hi", "hello", "menu", "start", "namaste"]:
            reply_msg.body(
                "🙏 Namaste 👋 Welcome to Vision Optical!\n\n"
                "Main aapki kya madad kar sakta hoon? Yeh options try karein:\n"
                "• *Chashma / Computer glasses*\n"
                "• *Eye test* (Appointment ke liye)\n"
                "• *Order status* (Apna order check karne ke liye)\n\n"
                "Ya seedha item ka naam likhein!"
            )

        # 2. Product Enquiry Flow (Example 1)
        elif "chashma" in msg or "glasses" in msg or "computer glasses" in msg:
            reply_msg.body(
                "Great 👍 ₹3,000 ke andar main aapko achhe options dikha sakta hoon.\n"
                "Aapko kis type ka chashma chahiye?\n\n"
                "1️⃣ Regular glasses\n"
                "2️⃣ Computer / Blue Cut\n"
                "3️⃣ Progressive\n"
                "4️⃣ Sunglasses"
            )
        
        elif "computer" in msg:
            reply_msg.body(
                "Sure 👍 Main ₹3,000 ke andar available computer glasses check karta hoon. Ek moment.\n\n"
                "👓 Ye options available hain:\n"
                "1. Titan Computer Frame + Blue Cut Lens — ₹2,499\n"
                "2. Fastrack Computer Frame + Blue Cut Lens — ₹2,799\n\n"
                "Kya aap photos dekhna chahenge? ('Yes' ya 'No' likhein)"
            )

        # 3. Eye-Test Booking Flow (Example 2)
        elif "eye test" in msg or "appointment" in msg or "test" in msg:
            reply_msg.body(
                "Bilkul 👁️ Main aapka eye-test appointment book karwa sakta hoon.\n"
                "Aap kis date ko aana chahenge? (Jaise: Kal evening)"
            )
        
        elif "kal evening" in msg or "evening" in msg:
            reply_msg.body(
                "Kal ke available evening slots:\n\n"
                "🕔 5:00 PM\n"
                "🕠 5:30 PM\n"
                "🕕 6:00 PM\n\n"
                "Kaunsa time convenient rahega?"
            )
        
        elif "5:30" in msg or "5.30" in msg:
            reply_msg.body(
                "Perfect 👍 Appointment confirm karne ke liye apna naam bata dijiye."
            )

        # 4. Order Status Flow (Example 3)
        elif "status" in msg or "ready" in msg or "chashma ready" in msg:
            reply_msg.body(
                "Bilkul, main aapka order status check karta hoon. 🔎\n\n"
                "Good news! 🎉\n"
                "Aapka order ready for pickup hai.\n\n"
                "📦 Order: #OPT10245\n"
                "👓 Product: Progressive Glasses\n"
                "📍 Vision Optical\n\n"
                "Aap store se pickup kar sakte hain."
            )

        # 5. Online Purchase / Order Flow (Example 4)
        elif "order karna" in msg or "titan frame" in msg or "buy" in msg:
            reply_msg.body(
                "Sure 👍\n"
                "Aapka selected product:\n\n"
                "👓 Titan Frame\n"
                "💰 ₹2,499\n\n"
                "Aap Store Pickup chahte hain ya Home Delivery?"
            )
        
        elif "home delivery" in msg or "delivery" in msg:
            reply_msg.body(
                "Great. Delivery ke liye aapka address confirm kar dijiye."
            )

        # General text handling or fallback
        else:
            reply_msg.body(
                f"🙏 Maaf kijiye, main samajh nahi paya. Vision Optical ke menu ke liye **'Menu'** type karke bhejiye."
            )

        return Response(content=str(resp), media_type="application/xml")
        
    except Exception as e:
        print(f"Error aaya: {str(e)}")
        return {"status": "error", "message": str(e)}
