import csv

import matplotlib.pyplot as plt

class LineItem:
    def __init__(self,
                 Date,
                 Product,
                 SKU,
                 Quantity,
                 UnitType,
                 PricePerUnit,
                 Multiplier,
                 Owner,
                 RepositorySlug,
                 Username,
                 ActionsWorkflow,
                 Notes):
        self.Date = Date
        self.Product = Product
        self.SKU = SKU
        self.Quantity = float(Quantity)
        self.UnitType = UnitType
        self.PricePerUnit = float(PricePerUnit)
        self.Multiplier = float(Multiplier)
        self.Owner = Owner
        self.RepositorySlug = RepositorySlug
        self.Username = Username
        self.ActionsWorkflow = ActionsWorkflow
        self.Notes = Notes
    
    def cost(self):
        return self.PricePerUnit * self.Quantity * self.Multiplier
    
    def workflowPath(self):
        return self.Owner + "/" + self.RepositorySlug + "/" + self.ActionsWorkflow
    
with open('example-report.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    line_items =[]
    for row in csv_reader:
        if line_count == 0:
            # ignore the first row containing headings
            line_count += 1
        else:
            line_items.append(LineItem(row[0],
                                   row[1],
                                   row[2],
                                   row[3],
                                   row[4],
                                   row[5],
                                   row[6],
                                   row[7],
                                   row[8],
                                   row[9],
                                   row[10],
                                   row[11]))
    workflow_costs = {}
    for item in line_items:
        if item.Product == "Actions":
            if item.workflowPath() in workflow_costs.keys():
                workflow_costs[item.workflowPath()] = workflow_costs[item.workflowPath()] + item.cost()
            else:
                workflow_costs.update({item.workflowPath():item.cost()})
    

    labels = list(workflow_costs.keys())
    values = list(workflow_costs.values())

    plt.pie(values, labels=labels)
    plt.show()


    



