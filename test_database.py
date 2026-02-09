#!/usr/bin/env python3
"""
Test script to verify database connection and form submission
"""

from run import app, db, JobApplication

def test_database():
    """Test database connection and basic operations"""
    with app.app_context():
        try:
            # Test 1: Check if table exists
            print("=== Testing Database Connection ===")
            db.create_all()
            print("✅ Database tables created/verified")
            
            # Test 2: Test basic insert
            print("\n=== Testing Basic Insert ===")
            test_app = JobApplication(
                job_id=999,
                job_title="Test Position",
                company="Test Company",
                first_name="Test",
                last_name="User",
                email="test@example.com",
                phone="123-456-7890",
                location="Test City",
                experience="1-3",
                education="bachelor",
                cover_letter="Test cover letter"
            )
            
            db.session.add(test_app)
            db.session.commit()
            print("✅ Test insert successful")
            
            # Test 3: Test query
            print("\n=== Testing Query ===")
            all_apps = JobApplication.query.all()
            print(f"✅ Found {len(all_apps)} applications in database")
            
            for app in all_apps:
                print(f"  - {app.first_name} {app.last_name} - {app.job_title}")
            
            # Test 4: Clean up test data
            print("\n=== Cleaning Up Test Data ===")
            db.session.delete(test_app)
            db.session.commit()
            print("✅ Test data cleaned up")
            
        except Exception as e:
            print(f"❌ Database error: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    test_database()
