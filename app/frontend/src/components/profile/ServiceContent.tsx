import { useRef, useState } from "react"
import ContentLayout from "./ContentLayout"
import ServiceCard from "./ServiceCard"
import Modal, { type TModalHandle } from "../ui/Modal"

const ServiceContent = () => {
  const serviceModalRef = useRef<TModalHandle>(null)
  const [selectedService, setSelectedService] = useState<number>()

  return (
    <>
      <ContentLayout
        title="Service(s) Provided"
        action={{
          label: "+ Add Service",
          onClick: () => serviceModalRef.current?.openModal(),
        }}
        children={
          <>
            <ServiceCard
              service={{
                id: 1,
                serviceId: 1,
                name: "Dog Grooming",
                description:
                  "Full grooming service including bath, haircut, nail trimming, and ear cleaning for all dog breeds.",
                rate: 80,
                duration: 120,
                days: [1, 2, 3, 4, 5],
              }}
              onEdit={(id: number) => console.log("Editing service: ", id)}
              onDelete={(id: number) => console.log("Deleting service: ", id)}
            />
            <ServiceCard
              service={{
                id: 1,
                serviceId: 1,
                name: "Cat Grooming",
                description:
                  "Gentle grooming for cats including bath, brushing, and nail trimming with specialized care.",
                rate: 50,
                duration: 60,
                days: [1, 2, 3, 4, 5],
              }}
              onEdit={(id: number) => console.log("Editing service: ", id)}
              onDelete={(id: number) => console.log("Deleting service: ", id)}
            />
          </>
        }
      />
      <Modal
        ref={serviceModalRef}
        header={`${selectedService ? "Edit" : "Add"} Service`}
        actionButtons={[
          {
            label: "Cancel",
            onClick: () => serviceModalRef.current?.closeModal(),
          },
          {
            label: selectedService ? "Save" : "Add",
            onClick: () => {
              serviceModalRef.current?.closeModal()
              console.log(selectedService ? "Saving service..." : "Adding service...")
            },
            style: "bg-blue-500 text-white hover:bg-blue-600",
          },
        ]}
      >
        Something will go here
      </Modal>
    </>
  )
}

export default ServiceContent
