import re

PRIORITY_KEYWORD={
        "high":[
            "server down", "system crash", "database error", "data loss",
            "security breach", "payment failed", "unable to login",
            "application not working", "website down", "critical bug",
            "network failure", "production issue", "urgent", "blocked",
            "cannot access", "crash", "failed", "stopped","defected","broken",

            # System & IT Critical
            "server down", "system down", "website down", "database error",
            "application crash", "system crash", "critical bug",
            "network outage", "internet down", "vpn not working",
            "production issue", "service unavailable", "data loss",

            # Access & Authentication
            "cannot login", "unable to login", "access denied",
            "account locked", "password reset urgent",

            # Security
            "security breach", "unauthorized access", "hacked",
            "virus detected", "malware", "phishing",

            # Business Impact
            "work blocked", "unable to work", "urgent",
            "critical", "high priority", "payment failed",
            "customer complaint", "client issue",

            # Hardware
            "computer not starting", "system not booting",
            "printer offline", "hard disk failure",

            # Finance
            "salary not credited", "payroll issue",
            "invoice failed", "transaction failed"
        ],
        "medium":[
                "slow", "performance issue", "bug", "incorrect data",
                "feature request", "sync issue", "delay", "not updating",
                "warning", "missing information", "page loading",
                "UI issue", "permission issue", "intermittent", "error",

                # Performance
                "slow", "lag", "performance issue",
                "page loading slowly", "delay",

                # Software
                "bug", "error message", "not updating",
                "sync issue", "incorrect data",
                "feature not working",

                # Access
                "permission issue", "role issue",
                "email issue", "outlook issue",

                # Hardware
                "printer issue", "scanner issue",
                "keyboard issue", "mouse issue",

                # HR
                "leave request", "attendance issue",
                "timesheet issue",

                # Operations
                "inventory mismatch", "stock issue",
                "workflow issue"

        ],
        "low":[
            "suggestion", "enhancement", "improvement",
            "cosmetic", "alignment", "color", "typo",
            "spelling mistake", "documentation", "minor issue",
            "layout", "small change", "feedback",

             # UI/UX
            "alignment", "color change",
            "layout issue", "font issue",
            "button size", "cosmetic issue",

            # Documentation
            "typo", "spelling mistake",
            "documentation update",

            # Improvements
            "enhancement", "suggestion",
            "feature request", "improvement",
            "optimization", "new feature",

            # General
            "feedback", "minor issue",
            "small change"
        ]
    }

high_pattern = re.compile(
    "|".join(re.escape(word) for word in PRIORITY_KEYWORD["high"])
    ,re.IGNORECASE) 

medium_pattern = re.compile(
    "|".join(re.escape(word) for word in PRIORITY_KEYWORD["medium"])
    ,re.IGNORECASE) 


low_pattern = re.compile(
    "|".join(re.escape(word) for word in PRIORITY_KEYWORD["low"]) 
    ,re.IGNORECASE)


def assign_priority(desc):

    if re.search(high_pattern,desc):
        return "high"
    
    if re.search(medium_pattern,desc):
        return "medium"
    
    if re.search(low_pattern,desc):
        return "low"
    
    return "low"
