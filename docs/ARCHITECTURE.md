# Technical Architecture: The "Pet-Diary" App (GCP)

This diagram outlines the Serverless Google Cloud architecture used to manage bookings, securely store pet data, and deliver the "Curated Daily Diary" (photos/videos) to owners.

```mermaid
graph TD
    %% Users
    Client("Pet Owner\n(Web/Mobile App)")
    Admin("Family/Staff\n(Admin Mobile App)")

    %% Frontend Hosting
    FirebaseHosting("Firebase Hosting\n(React/Flutter Web)")

    %% API & Compute
    subgraph Google Cloud Platform
        CloudRun("Cloud Run\n(Node.js / Go API)")
        Auth("Firebase Auth\n(Identity)")
        
        %% Databases
        Firestore("Cloud Firestore\n(NoSQL)")
        CloudStorage("Cloud Storage\n(Media: Photos/Videos)")
        
        %% Background Processing
        PubSub("Cloud Pub/Sub\n(Event Bus)")
        CloudFunctions("Cloud Functions\n(Background Tasks)")
    end

    %% External Services
    Stripe("Payment Gateway\n(Stripe / Przelewy24)")
    Push("Firebase Cloud Messaging\n(Push Notifications)")

    %% Connections - Client Side
    Client -->|Logs in| Auth
    Client -->|Loads App| FirebaseHosting
    Client -->|Books Stay / Views Diary| CloudRun
    Client -->|Downloads Photos| CloudStorage

    %% Connections - Admin Side
    Admin -->|Uploads Daily Photos| CloudStorage
    Admin -->|Logs Activity / Status| CloudRun

    %% Connections - Backend Logic
    CloudRun -->|Reads/Writes Profiles & Bookings| Firestore
    CloudRun -->|Initiates Payment| Stripe
    CloudStorage -->|Triggers Resize/Thumbnail Event| PubSub
    PubSub --> CloudFunctions
    CloudFunctions -->|Updates DB with Image URL| Firestore
    CloudFunctions -->|Sends 'New Photo!' Alert| Push
    Push -.-> Client
```

### Key Components:
1. **Firestore:** Stores structured data (Pet Profiles, Vaccination expiries, Booking dates, "Diary" text entries).
2. **Cloud Storage:** Stores the high-res photos and videos taken by the family.
3. **Cloud Functions:** Triggers automatically when a new photo is uploaded, creates a thumbnail, and sends a Push Notification to the owner's phone saying "Fido is having a great time! Tap to see today's photo."
