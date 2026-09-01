from fastapi import FastAPI, Request, Response, Form
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

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

        # ==================== EXAMPLE 1: Product Enquiry Flow ====================
        if "chashma chahiye" in msg:
            reply_msg.body(
                "Namaste 👋 Welcome to Vision Optical!\n"
                "Bilkul, main aapko suitable glasses choose karne mein help karta hoon.\n"
                "Aapka budget approximately kitna hai?"
            )

        elif any(word in msg for word in ["hi", "hello", "menu", "start", "namaste"]):
            reply_msg.body(
                "🙏 Namaste 👋 Welcome to Vision Optical!\n\n"
                "Aap kya karna chahte hain? Inme se batayein:\n"
                "• Chashma kharidna hai (Budget batayein)\n"
                "• Eye test karwana hai\n"
                "• Mera chashma ready hua? (Order status)\n"
                "• Mujhe ye frame order karna hai"
            )

        elif "3000" in msg or "budget" in msg:
            reply_msg.body(
                "Great 👍 ₹3,000 ke andar main aapko achhe options dikha sakta hoon.\n"
                "Aapko kis type ka chashma chahiye?\n\n"
                "1️⃣ Regular glasses\n"
                "2️⃣ Computer / Blue Cut\n"
                "3️⃣ Progressive\n"
                "4️⃣ Sunglasses"
            )

        elif "computer glasses" in msg or "computer" in msg:
            reply_msg.body(
                "Sure 👍 Main ₹3,000 ke andar available computer glasses check karta hoon. Ek moment.\n\n"
                "👓 Ye options available hain:\n\n"
                "1. Titan Computer Frame + Blue Cut Lens — ₹2,499\n"
                "2. Fastrack Computer Frame + Blue Cut Lens — ₹2,799\n\n"
                "Kya aap photos dekhna chahenge?"
            )

        # ==================== EXAMPLE 2: Eye-test Booking Flow ====================
        elif "eye test" in msg or "eye-test" in msg or "test karwana hai" in msg:
            reply_msg.body(
                "Bilkul 👁️ Main aapka eye-test appointment book karwa sakta hoon.\n"
                "Aap kis date ko aana chahenge?"
            )

        elif "kal evening" in msg or "evening" in msg or "kal" in msg:
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

        # Final Appointment Confirmation
        elif "confirm appointment" in msg or msg == "confirm":
            reply_msg.body(
                "✅ Appointment confirmed!\n\n"
                "We look forward to seeing you at Vision Optical. 👓"
            )

        # ==================== EXAMPLE 3: Order Status Flow ====================
        elif "ready" in msg or "status" in msg or "chashma ready hua" in msg:
            reply_msg.body(
                "Bilkul, main aapka order status check karta hoon. 🔎\n\n"
                "Good news! 🎉\n"
                "Aapka order ready for pickup hai.\n\n"
                "📦 Order: #OPT10245\n"
                "👓 Product: Progressive Glasses\n"
                "📍 Vision Optical\n\n"
                "Aap store se pickup kar sakte hain."
            )

        # ==================== EXAMPLE 4: Online Purchase Flow ====================
        elif "frame order karna hai" in msg or "mujhe ye frame" in msg or "titan frame" in msg:
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

        elif any(addr in msg for addr in ["address", "street", "sector", "allahabad", "delhi", "kanpur", "house", "flat"]):
            reply_msg.body(
                "Order summary:\n\n"
                "👓 Titan Frame + Blue Cut Lens — ₹2,499\n"
                "🚚 Delivery — ₹100\n"
                "Total — ₹2,599\n\n"
                "Kya aap payment ke liye proceed karna chahenge?"
            )

        # Payment Link for Online Purchase
        elif "pay" in msg or "payment" in msg or "proceed" in msg or msg == "yes":
            reply_msg.body(
                "Perfect. 💳 Aapka secure payment link:\n\n"
                "Pay ₹2,599\n\n"
                "Payment complete hone ke baad aapka order automatically confirm ho jayega."
            )

        # Name Capture for Booking (Fallback for single-word names if typing after slot)
        elif len(msg.split()) == 1 and not any(w in msg for w in ["hi", "hello", "menu", "status", "delivery", "frame", "yes"]):
            name = Body.strip().capitalize()
            reply_msg.body(
                f"Thank you, {name}.\n\n"
                f"👁️ Eye Test Appointment\n"
                f"📅 2 September\n"
                f"🕠 5:30 PM\n"
                f"👤 {name}\n\n"
                "Appointment confirm karne ke liye **'Confirm'** type karein."
            )

        # Fallback / Default response
        else:
            reply_msg.body(
                "🙏 Maaf kijiye, main samajh nahi paya. Vision Optical ke menu ke liye **'Menu'** type karke bhejiye."
            )

        return Response(content=str(resp), media_type="application/xml")
        
    except Exception as e:
        print(f"Error aaya: {str(e)}")
        return {"status": "error", "message": str(e)}
