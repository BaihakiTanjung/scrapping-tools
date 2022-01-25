function scrappingData(url) {
    fetch(url)
        .then(response => response.json())
        .then(data => { return data })
}

console.log(scrappingData("https://api-v2.segari.id/v1.1/products/price?agentId=311&tagIds=1&tagIds=158&tagIds=2&tagIds=156&tagIds=3&tagIds=157&size=40&page=1&paginationType=slice&deliveryDate=2022-01-27&deliveryServiceType=NEXT_DAY_DELIVERY&availableDeliveryDates=2022-01-26,2022-01-27,2022-01-28"))